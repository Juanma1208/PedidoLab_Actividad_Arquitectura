from datetime import datetime
from pedidolabs.pedido import Pedido
from pedidolabs.reportes import generar_reporte_ventas

def construir(cliente, total, estado="CONFIRMADO"):
    p = Pedido("P1", cliente, "x", "Manizales", "Caldas", "170001")
    p.total_pagado = total
    p.estado = estado
    p.fecha = datetime(2026, 10, 20, 12, 0, 0)
    return p

def test_reporte_resume_ventas(cliente_premium, cliente_normal):
    pedidos = [construir(cliente_premium, 200_000), construir(cliente_normal, 100_000)]
    r = generar_reporte_ventas(pedidos, "2026-10-01", "2026-10-31")
    assert "Pedidos confirmados: 2" in r
    assert "Total vendido: $300,000" in r
    assert "Clientes PREMIUM: 1" in r

def test_reporte_ignora_no_confirmados(cliente_normal):
    r = generar_reporte_ventas(
        [construir(cliente_normal, 100_000, "CANCELADO")],
        "2026-10-01", "2026-10-31"
    )
    assert "Pedidos confirmados: 0" in r

def test_reporte_incluye_detalle(cliente_normal):
    r = generar_reporte_ventas(
        [construir(cliente_normal, 100_000)],
        "2026-10-01", "2026-10-31", incluir_detalle=True
    )
    assert "DETALLE" in r
    assert "Nora" in r
