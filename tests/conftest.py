import pytest
from pedidolabs.cliente import Cliente
from pedidolabs.producto import Producto
from pedidolabs.pedido import Pedido
from pedidolabs.inventario import Inventario

@pytest.fixture
def cliente_normal():
    return Cliente("1", "Nora", "nora@test.com", "3001", "NORMAL")

@pytest.fixture
def cliente_premium():
    return Cliente("2", "Paula", "paula@test.com", "3002", "PREMIUM")

@pytest.fixture
def cliente_corporativo():
    return Cliente("3", "Corp SA", "corp@test.com", "3003", "CORPORATIVO")

@pytest.fixture
def producto_a():
    return Producto("A", "Producto A", 100_000, 1.0)

@pytest.fixture
def producto_b():
    return Producto("B", "Producto B", 250_000, 2.5)

@pytest.fixture
def pedido_premium(cliente_premium, producto_a):
    p = Pedido("PX", cliente_premium, "Calle 1", "Manizales", "Caldas", "170001")
    p.agregar_item(producto_a, 3)
    return p

@pytest.fixture
def inventario():
    return Inventario({"A": 10, "B": 5})
