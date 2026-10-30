import pytest
from pedidolabs.pedido import Pedido
from pedidolabs.envios import calcular_costo_envio

def test_envio_manizales_base(cliente_normal, producto_a):
    p = Pedido("1", cliente_normal, "x", "Manizales", "Caldas", "170001")
    p.agregar_item(producto_a, 1)
    assert calcular_costo_envio(p) == 8_000

def test_envio_fuera_de_caldas(cliente_normal, producto_a):
    p = Pedido("1", cliente_normal, "x", "Pereira", "Risaralda", "660001")
    p.agregar_item(producto_a, 1)
    assert calcular_costo_envio(p) == 18_000

def test_envio_incrementa_por_peso(cliente_normal, producto_b):
    p = Pedido("1", cliente_normal, "x", "Manizales", "Caldas", "170001")
    p.agregar_item(producto_b, 3)
    assert calcular_costo_envio(p) == 16_000

def test_envio_gratis_premium_por_subtotal_alto(cliente_premium, producto_b):
    p = Pedido("1", cliente_premium, "x", "Manizales", "Caldas", "170001")
    p.agregar_item(producto_b, 3)
    assert calcular_costo_envio(p) == 0

def test_modalidad_no_soportada(pedido_premium):
    with pytest.raises(ValueError):
        calcular_costo_envio(pedido_premium, "EXPRESS")
