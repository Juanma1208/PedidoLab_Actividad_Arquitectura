import pytest
from pedidolabs.stockcloud_api import StockCloudAPI
from pedidolabs.inventario_stockcloud import StockCloudInventario


def test_stockcloud_traduce_errores_a_valueerror():
    inv = StockCloudInventario(StockCloudAPI({"A": 1}))
    with pytest.raises(ValueError):
        inv.reservar("Z", 1)


def test_stockcloud_reserva_descuenta_stock():
    api = StockCloudAPI({"A": 5})
    inv = StockCloudInventario(api)
    inv.reservar("A", 2)
    assert api.query_stock("A")["available_units"] == 3