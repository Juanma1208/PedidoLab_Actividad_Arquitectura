class PayFastAPI:
    """Simulación de una API externa que no controlamos."""

    def __init__(self, merchant_code="PEDIDOLAB-001"):
        self.merchant_code = merchant_code
        self._contador = 0

    def make_transaction(self, card_number, amount, currency, merchant_code):
        if merchant_code != self.merchant_code:
            return {"code": 91, "message": "merchant not found"}
        if not card_number or len(card_number) < 8:
            return {"code": 14, "message": "invalid card"}
        if amount <= 0:
            return {"code": 13, "message": "invalid amount"}
        self._contador += 1
        return {
            "code": 0,
            "message": "approved",
            "transaction_id": f"PF-{self._contador:05d}",
        }


def cobrar_con_payfast(api, numero_tarjeta, monto):
    resultado = api.make_transaction(
        card_number=numero_tarjeta,
        amount=monto,
        currency="COP",
        merchant_code="PEDIDOLAB-001",
    )
    if resultado["code"] == 0:
        return resultado["transaction_id"]
    if resultado["code"] == 14:
        raise ValueError("Tarjeta inválida")
    if resultado["code"] == 13:
        raise ValueError("Monto inválido")
    raise RuntimeError(f"Pago rechazado: {resultado['message']}")


class AdaptadorPayFast:
    """Adapter: traduce el puerto de PedidoLab al contrato concreto de PayFast."""

    def __init__(self, api=None):
        self.api = api or PayFastAPI()

    def cobrar(self, numero_tarjeta: str, monto: float) -> str:
        return cobrar_con_payfast(
            self.api,
            numero_tarjeta=numero_tarjeta,
            monto=monto,
        )
