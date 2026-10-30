def calcular_costo_envio(pedido, modalidad="ESTANDAR"):
    # Deliberadamente conoce demasiados detalles internos de Pedido.
    ciudad = pedido.ciudad.upper()
    departamento = pedido.departamento.upper()

    peso = 0.0
    for item in pedido.items:
        peso += item.producto.peso * item.cantidad

    subtotal = 0.0
    for item in pedido.items:
        subtotal += item.producto.precio * item.cantidad

    tipo_cliente = pedido.cliente.tipo

    if modalidad != "ESTANDAR":
        raise ValueError("Modalidad de envío no soportada")

    if subtotal >= 700_000 and tipo_cliente in ("PREMIUM", "CORPORATIVO"):
        return 0.0

    if departamento == "CALDAS":
        if ciudad == "MANIZALES":
            base = 8_000.0
        else:
            base = 12_000.0
    else:
        base = 18_000.0

    if peso > 10:
        base += 15_000.0
    elif peso > 5:
        base += 8_000.0
    elif peso > 2:
        base += 4_000.0
    return base
