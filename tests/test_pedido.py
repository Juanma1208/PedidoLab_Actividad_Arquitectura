import pytest
from pedidolabs.pedido import Pedido

def test_agregar_item_y_subtotal(cliente_normal, producto_a):
    p = Pedido("1", cliente_normal, "x", "Manizales", "Caldas", "170001")
    p.agregar_item(producto_a, 2)
    assert p.subtotal() == 200_000

def test_peso_total(cliente_normal, producto_b):
    p = Pedido("1", cliente_normal, "x", "Manizales", "Caldas", "170001")
    p.agregar_item(producto_b, 2)
    assert p.peso_total() == 5.0

def test_no_permite_cantidad_cero(cliente_normal, producto_a):
    p = Pedido("1", cliente_normal, "x", "Manizales", "Caldas", "170001")
    with pytest.raises(ValueError):
        p.agregar_item(producto_a, 0)

def test_direccion_entrega(cliente_normal):
    p = Pedido("1", cliente_normal, "Calle 10", "Pereira", "Risaralda", "660001")
    assert p.direccion_entrega() == "Calle 10, Pereira, Risaralda, 660001"
