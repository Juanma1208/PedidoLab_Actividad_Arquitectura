from pedidolabs.notificaciones import (
    MENSAJES_ENVIADOS, limpiar_bandeja, enviar_email_confirmacion,
    enviar_email_pago, enviar_email_cancelacion
)

def setup_function():
    limpiar_bandeja()

def test_confirmacion_registra_email(cliente_normal):
    texto = enviar_email_confirmacion(cliente_normal, "P1", 120_000)
    assert "P1" in texto
    assert MENSAJES_ENVIADOS[0]["destino"] == cliente_normal.email

def test_pago_incluye_transaccion(cliente_normal):
    texto = enviar_email_pago(cliente_normal, "P1", "TX-1", 120_000)
    assert "TX-1" in texto

def test_cancelacion(cliente_normal):
    texto = enviar_email_cancelacion(cliente_normal, "P1")
    assert "cancelado" in texto.lower()

def test_limpieza_bandeja(cliente_normal):
    enviar_email_confirmacion(cliente_normal, "P1", 100)
    limpiar_bandeja()
    assert MENSAJES_ENVIADOS == []
