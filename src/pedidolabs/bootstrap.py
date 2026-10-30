"""Composition Root de PedidoLab.

Este módulo conoce los detalles concretos y ensambla la aplicación.
La lógica de aplicación no necesita importarlos.
"""

from .notificaciones import NotificadorEmail
from .pagos import AdaptadorPayFast, PayFastAPI
from .repositorio import RepositorioArchivo
from .servicio_pedidos import ServicioPedidos


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
