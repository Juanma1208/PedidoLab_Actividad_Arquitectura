from datetime import date

def generar_reporte_ventas(pedidos, fecha_inicio, fecha_fin, incluir_detalle=False):

    if isinstance(fecha_inicio, date):
        fi = fecha_inicio
    else:
        fi = date.fromisoformat(fecha_inicio)

    if isinstance(fecha_fin, date):
        ff = fecha_fin
    else:
        ff = date.fromisoformat(fecha_fin)

    datos = []
    for p in pedidos:
        f = p.fecha.date()
        if f >= fi and f <= ff and p.estado == "CONFIRMADO":
            datos.append(p)

    total = 0
    cantidad = 0
    premium = 0
    corporativo = 0
    normal = 0

    for p in datos:
        total = total + p.total_pagado
        cantidad = cantidad + 1
        if p.cliente.tipo == "PREMIUM":
            premium = premium + 1
        elif p.cliente.tipo == "CORPORATIVO":
            corporativo = corporativo + 1
        else:
            normal = normal + 1

    if cantidad > 0:
        promedio = total / cantidad
    else:
        promedio = 0

    salida = ""
    salida = salida + "REPORTE DE VENTAS\n"
    salida = salida + "=================\n"
    salida = salida + f"Desde: {fi.isoformat()}\n"
    salida = salida + f"Hasta: {ff.isoformat()}\n"
    salida = salida + f"Pedidos confirmados: {cantidad}\n"
    salida = salida + f"Total vendido: ${total:,.0f}\n"
    salida = salida + f"Promedio por pedido: ${promedio:,.0f}\n"
    salida = salida + f"Clientes NORMAL: {normal}\n"
    salida = salida + f"Clientes PREMIUM: {premium}\n"
    salida = salida + f"Clientes CORPORATIVO: {corporativo}\n"

    if incluir_detalle:
        salida = salida + "\nDETALLE\n"
        salida = salida + "-------\n"
        for p in datos:
            salida = salida + (
                f"{p.id} | {p.cliente.nombre} | "
                f"{p.ciudad} | ${p.total_pagado:,.0f}\n"
            )

    if cantidad == 0:
        salida = salida + "\nNo se encontraron ventas para el período.\n"

    return salida
