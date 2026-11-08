import ast
import inspect
from pedidolabs import servicio_pedidos
from pedidolabs.bootstrap import crear_inventario, crear_servicio_pedidos
from pedidolabs.notificaciones import limpiar_bandeja
from pedidolabs.producto import Producto

PRODUCTO_A = Producto("A", "Producto A", 100000, 1.0)
ARGS = (
    "P1", "1", "Ana", "ana@test.com", "300", "NORMAL",
    "Calle 1", "Manizales", "Caldas", "170001",
    [(PRODUCTO_A, 2)], "4111111111111111",
)


class InventarioFalso:
    def validar_disponibilidad(self, codigo, cantidad):
        return True

    def reservar(self, codigo, cantidad):
        pass


def test_stockcloud_queda_detras_de_adaptador(tmp_path):
    limpiar_bandeja()
    inventario = crear_inventario("stockcloud", {"A": 10})
    servicio = crear_servicio_pedidos(inventario, tmp_path / "pedidos.jsonl")
    servicio.procesar_pedido(*ARGS)
    assert inventario.api.query_stock("A")["available_units"] == 8


def test_nucleo_procesa_sin_stockcloud(tmp_path):
    limpiar_bandeja()
    servicio = crear_servicio_pedidos(InventarioFalso(), tmp_path / "pedidos.jsonl")
    pedido = servicio.procesar_pedido(*ARGS)
    assert pedido.estado == "CONFIRMADO"


def test_servicio_no_importa_stockcloud():
    arbol = ast.parse(inspect.getsource(servicio_pedidos))
    modulos = set()
    for nodo in ast.walk(arbol):
        if isinstance(nodo, ast.Import):
            modulos.update(alias.name for alias in nodo.names)
        elif isinstance(nodo, ast.ImportFrom):
            modulos.add(nodo.module or "")
            modulos.update(alias.name for alias in nodo.names)
    assert not any("stockcloud" in m.lower() for m in modulos)