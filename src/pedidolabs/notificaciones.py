MENSAJES_ENVIADOS = []


def enviar_email_confirmacion(cliente, pedido_id, total):
    asunto = f"Confirmación pedido {pedido_id}"
    cuerpo = (
        f"Hola {cliente.nombre}, su pedido {pedido_id} fue confirmado. "
        f"Total pagado: ${total:,.0f}."
    )
    MENSAJES_ENVIADOS.append(
        {"canal": "EMAIL", "destino": cliente.email, "asunto": asunto, "cuerpo": cuerpo}
    )
    return cuerpo


def enviar_email_pago(cliente, pedido_id, transaccion_id, total):
    asunto = f"Pago recibido {pedido_id}"
    cuerpo = (
        f"Hola {cliente.nombre}, recibimos el pago del pedido {pedido_id}. "
        f"Transacción {transaccion_id}. Total: ${total:,.0f}."
    )
    MENSAJES_ENVIADOS.append(
        {"canal": "EMAIL", "destino": cliente.email, "asunto": asunto, "cuerpo": cuerpo}
    )
    return cuerpo


def enviar_email_cancelacion(cliente, pedido_id):
    asunto = f"Pedido cancelado {pedido_id}"
    cuerpo = f"Hola {cliente.nombre}, el pedido {pedido_id} fue cancelado."
    MENSAJES_ENVIADOS.append(
        {"canal": "EMAIL", "destino": cliente.email, "asunto": asunto, "cuerpo": cuerpo}
    )
    return cuerpo


def limpiar_bandeja():
    MENSAJES_ENVIADOS.clear()


class NotificadorEmail:
    """Colaborador concreto que encapsula las funciones de notificación existentes."""

    def pago_recibido(self, cliente, pedido_id, transaccion_id, total):
        return enviar_email_pago(cliente, pedido_id, transaccion_id, total)

    def pedido_confirmado(self, cliente, pedido_id, total):
        return enviar_email_confirmacion(cliente, pedido_id, total)
