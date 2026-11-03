"""Composition Root de PedidoLab.

Este módulo conoce los detalles concretos y ensambla la aplicación.
La lógica de aplicación no necesita importarlos.
"""

from .notificaciones import NotificadorEmail
from .pagos import AdaptadorPayFast, PayFastAPI
from .repositorio import RepositorioArchivo
from .servicio_pedidos import ServicioPedidos
from .inventario import Inventario
from .inventario_stockcloud import StockCloudInventario
from .stockcloud_api import StockCloudAPI


def crear_servicio_pedidos(inventario, ruta_pedidos="pedidos.jsonl"):
    repositorio = RepositorioArchivo(ruta_pedidos)
    procesador_pago = AdaptadorPayFast(PayFastAPI())
    notificador = NotificadorEmail()

    return ServicioPedidos(
        inventario=inventario,
        repositorio=repositorio,
        procesador_pago=procesador_pago,
        notificador=notificador,
    )

def crear_inventario(tipo, stock_inicial):
    if tipo == "local":
        return Inventario(stock_inicial)
    if tipo == "stockcloud":
        return StockCloudInventario(StockCloudAPI(stock_inicial))
    raise ValueError(f"Tipo de inventario desconocido: {tipo}")