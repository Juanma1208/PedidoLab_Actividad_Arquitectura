class StockCloudAPI:
    """API externa simulada. En la actividad se considera código de un proveedor.

    No debe modificarse. La aplicación debe adaptarse a esta interfaz.
    """

    def __init__(self, stock_inicial=None):
        self._stock = dict(stock_inicial or {})

    def query_stock(self, sku: str) -> dict:
        if sku not in self._stock:
            return {"status": "NOT_FOUND", "sku": sku, "available_units": 0}
        return {"status": "OK", "sku": sku, "available_units": self._stock[sku]}

    def reserve_units(self, sku: str, units: int) -> dict:
        if units <= 0:
            return {"status": "INVALID_UNITS", "sku": sku}
        if sku not in self._stock:
            return {"status": "NOT_FOUND", "sku": sku}
        if self._stock[sku] < units:
            return {
                "status": "INSUFFICIENT_STOCK",
                "sku": sku,
                "available_units": self._stock[sku],
                "requested_units": units,
            }
        self._stock[sku] -= units
        return {
            "status": "RESERVED",
            "sku": sku,
            "remaining_units": self._stock[sku],
        }
