import pytest

def test_validar_disponibilidad(inventario):
    assert inventario.validar_disponibilidad("A", 2)

def test_reservar_reduce_stock(inventario):
    inventario.reservar("A", 3)
    assert inventario.disponible("A") == 7

def test_no_permite_reservar_mas_de_lo_disponible(inventario):
    with pytest.raises(ValueError):
        inventario.reservar("B", 99)

def test_devolver_restaura_stock(inventario):
    inventario.reservar("A", 2)
    inventario.devolver("A", 2)
    assert inventario.disponible("A") == 10

def test_producto_inexistente(inventario):
    with pytest.raises(ValueError):
        inventario.disponible("Z")
