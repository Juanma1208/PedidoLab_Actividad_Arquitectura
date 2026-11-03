from .producto import Producto

def mapear_pedido(datos: dict) -> dict:
    kwargs = {k: v for k, v in datos.items() if k != "items"}
    kwargs["items"] = [
        (Producto(i["codigo"], i["nombre"], i["precio"], i["peso"]), i["cantidad"])
        for i in datos["items"]
    ]
    return kwargs

def manejar_post_pedido(datos: dict, caso_uso) -> tuple[int, dict]:
    try:
        pedido = caso_uso.procesar_pedido(**mapear_pedido(datos))
    except KeyError as error:
        return 400, {"error": f"Falta el campo {error}"}
    except ValueError as error:
        return 400, {"error": str(error)}
    except RuntimeError as error:
        return 402, {"error": str(error)}
    return 201, {
        "pedido_id": pedido.id,
        "estado": pedido.estado,
        "total": pedido.total_pagado,
    }