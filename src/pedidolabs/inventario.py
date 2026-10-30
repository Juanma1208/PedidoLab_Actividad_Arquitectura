class Inventario:
    def __init__(self, stock_inicial=None):
        self.stock = dict(stock_inicial or {})

    def validar_disponibilidad(self, codigo, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if codigo not in self.stock:
            raise ValueError(f"Producto {codigo} no existe en inventario")
        if self.stock[codigo] < cantidad:
            raise ValueError(
                f"Stock insuficiente para {codigo}: "
                f"disponible={self.stock[codigo]}, solicitado={cantidad}"
            )
        return True

    def reservar(self, codigo, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if codigo not in self.stock:
            raise ValueError(f"Producto {codigo} no existe en inventario")
        if self.stock[codigo] < cantidad:
            raise ValueError(
                f"Stock insuficiente para {codigo}: "
                f"disponible={self.stock[codigo]}, solicitado={cantidad}"
            )
        self.stock[codigo] = self.stock[codigo] - cantidad

    def devolver(self, codigo, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if codigo not in self.stock:
            raise ValueError(f"Producto {codigo} no existe en inventario")
        self.stock[codigo] = self.stock[codigo] + cantidad

    def ajustar(self, codigo, cantidad):
        if cantidad < 0:
            raise ValueError("El ajuste no puede ser negativo")
        if codigo not in self.stock:
            raise ValueError(f"Producto {codigo} no existe en inventario")
        self.stock[codigo] = cantidad

    def disponible(self, codigo):
        if codigo not in self.stock:
            raise ValueError(f"Producto {codigo} no existe en inventario")
        return self.stock[codigo]
