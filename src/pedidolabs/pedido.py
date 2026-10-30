from dataclasses import dataclass
from datetime import datetime
from .producto import Producto

@dataclass
class ItemPedido:
    producto: Producto
    cantidad: int

    def total(self) -> float:
        return self.producto.precio * self.cantidad

    def peso_total(self) -> float:
        return self.producto.peso * self.cantidad

class Pedido:
    def __init__(self, pedido_id, cliente, calle, ciudad, departamento, codigo_postal):
        self.id = pedido_id
        self.cliente = cliente
        self.items = []
        self.calle = calle
        self.ciudad = ciudad
        self.departamento = departamento
        self.codigo_postal = codigo_postal
        self.estado = "CREADO"
        self.fecha = datetime.now()
        self.transaccion_id = None
        self.total_pagado = 0.0

    def agregar_item(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.items.append(ItemPedido(producto, cantidad))

    def subtotal(self):
        return sum(i.producto.precio * i.cantidad for i in self.items)

    def peso_total(self):
        return sum(i.producto.peso * i.cantidad for i in self.items)

    def cantidad_total(self):
        return sum(i.cantidad for i in self.items)

    def direccion_entrega(self):
        partes = [self.calle.strip(), self.ciudad.strip(),
                  self.departamento.strip(), self.codigo_postal.strip()]
        return ", ".join(p for p in partes if p)
