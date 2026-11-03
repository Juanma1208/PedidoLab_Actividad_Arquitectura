class StockCloudInventario:
    def __init__(self, api):
        self.api = api

    def validar_disponibilidad(self, codigo: str, cantidad: int) -> bool:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        respuesta = self.api.query_stock(codigo)
        if respuesta["status"] != "OK":
            raise ValueError(f"Producto {codigo} no existe en inventario")
        if respuesta["available_units"] < cantidad:
            raise ValueError(
                f"Stock insuficiente para {codigo}: "
                f"disponible={respuesta['available_units']}, solicitado={cantidad}"
            )
        return True

    def reservar(self, codigo: str, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        respuesta = self.api.reserve_units(codigo, cantidad)
        if respuesta["status"] != "RESERVED":
            raise ValueError(f"No se pudo reservar {codigo}: {respuesta['status']}")