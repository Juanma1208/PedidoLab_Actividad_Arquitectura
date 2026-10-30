def calcular_descuento(cliente, subtotal):
    if cliente.tipo == "NORMAL":
        return 0.0
    if cliente.tipo == "PREMIUM":
        if subtotal >= 500_000:
            return subtotal * 0.15
        return subtotal * 0.10
    if cliente.tipo == "CORPORATIVO":
        if subtotal >= 1_000_000:
            return subtotal * 0.20
        return subtotal * 0.12
    return 0.0

def descripcion_descuento(cliente, subtotal):
    if cliente.tipo == "NORMAL":
        return "Sin descuento"
    if cliente.tipo == "PREMIUM":
        if subtotal >= 500_000:
            return "Cliente PREMIUM: 15%"
        return "Cliente PREMIUM: 10%"
    if cliente.tipo == "CORPORATIVO":
        if subtotal >= 1_000_000:
            return "Cliente CORPORATIVO: 20%"
        return "Cliente CORPORATIVO: 12%"
    return "Sin descuento"

def calcular_beneficio_fidelidad(cliente, total):
    if cliente.tipo == "NORMAL":
        return int(total // 50_000)
    if cliente.tipo == "PREMIUM":
        return int(total // 25_000)
    if cliente.tipo == "CORPORATIVO":
        return int(total // 20_000)
    return 0

def calcular_total_con_descuento(pedido):
    subtotal = pedido.subtotal()
    return subtotal - calcular_descuento(pedido.cliente, subtotal)
