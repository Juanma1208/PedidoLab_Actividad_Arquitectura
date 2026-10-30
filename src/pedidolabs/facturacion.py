def generar_factura(pedido, subtotal, descuento, envio):
    total = subtotal - descuento + envio
    return "\n".join([
        f"FACTURA {pedido.id}",
        f"Cliente: {pedido.cliente.nombre}",
        f"Documento: {pedido.cliente.documento}",
        f"Subtotal: ${subtotal:,.0f}",
        f"Descuento: ${descuento:,.0f}",
        f"Envío: ${envio:,.0f}",
        f"TOTAL: ${total:,.0f}",
    ])
