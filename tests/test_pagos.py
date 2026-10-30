import pytest
from pedidolabs.pagos import PayFastAPI, cobrar_con_payfast

def test_pago_aprobado_retorna_transaccion():
    api = PayFastAPI()
    tx = cobrar_con_payfast(api, "4111111111111111", 100_000)
    assert tx.startswith("PF-")

def test_tarjeta_invalida():
    with pytest.raises(ValueError, match="Tarjeta inválida"):
        cobrar_con_payfast(PayFastAPI(), "123", 100_000)

def test_monto_invalido():
    with pytest.raises(ValueError, match="Monto inválido"):
        cobrar_con_payfast(PayFastAPI(), "4111111111111111", 0)

def test_api_externa_rechaza_comercio_incorrecto():
    r = PayFastAPI().make_transaction("4111111111111111", 1000, "COP", "OTRO")
    assert r["code"] == 91
