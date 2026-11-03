from pedidolabs.entradas import manejar_post_pedido, procesar_lote

DATOS = {
    "pedido_id": "P-100", "documento": "10", "nombre": "Ana",
    "email": "ana@test.com", "telefono": "300", "tipo_cliente": "NORMAL",
    "calle": "Calle 1", "ciudad": "Manizales", "departamento": "Caldas",
    "codigo_postal": "170001",
    "items": [{"codigo": "A", "nombre": "Producto A", "precio": 100000,
               "peso": 1.0, "cantidad": 2}],
    "numero_tarjeta": "4111111111111111", "enviar_confirmacion": True,
}


class PedidoFalso:
    def __init__(self, id, total):
        self.id = id
        self.estado = "CONFIRMADO"
        self.total_pagado = total


class CasoUsoFalso:
    def __init__(self, total=999, error=None):
        self.llamadas = []
        self.total = total
        self.error = error

    def procesar_pedido(self, **kwargs):
        self.llamadas.append(kwargs)
        if self.error:
            raise self.error
        return PedidoFalso(kwargs["pedido_id"], self.total)

class CasoUsoSelectivo(CasoUsoFalso):
    def procesar_pedido(self, **kwargs):
        if kwargs["pedido_id"] == "P-MAL":
            self.llamadas.append(kwargs)
            raise ValueError("Stock insuficiente para A")
        return super().procesar_pedido(**kwargs)

def test_rest_delega_al_caso_de_uso_sin_recalcular():
    fake = CasoUsoFalso(total=999)
    status, cuerpo = manejar_post_pedido(DATOS, fake)

    assert status == 201
    assert len(fake.llamadas) == 1
    producto, cantidad = fake.llamadas[0]["items"][0]
    assert producto.precio == 100000 and cantidad == 2
    assert cuerpo["total"] == 999  # el adapter no calcula el total


def test_error_de_negocio_se_traduce_a_400():
    fake = CasoUsoFalso(error=ValueError("Stock insuficiente para A"))
    status, cuerpo = manejar_post_pedido(DATOS, fake)

    assert status == 400
    assert "Stock insuficiente" in cuerpo["error"]

def test_batch_y_rest_usan_la_misma_capacidad():
    fake_rest = CasoUsoFalso()
    fake_batch = CasoUsoFalso()
    manejar_post_pedido(DATOS, fake_rest)
    procesar_lote([DATOS], fake_batch)
    assert fake_rest.llamadas == fake_batch.llamadas


def test_batch_registra_error_y_sigue_con_el_resto():
    fake = CasoUsoSelectivo()
    resumen = procesar_lote([{**DATOS, "pedido_id": "P-MAL"}, DATOS], fake)
    assert resumen["ok"] == 1
    assert resumen["errores"][0]["pedido_id"] == "P-MAL"