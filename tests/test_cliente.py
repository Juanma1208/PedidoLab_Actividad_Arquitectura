from pedidolabs.cliente import Cliente

def test_direccion_completa():
    c = Cliente("1", "Ana", "a@x.com", "300", "NORMAL",
                "Calle 1", "Manizales", "Caldas", "170001")
    assert c.direccion_completa() == "Calle 1, Manizales, Caldas, 170001"

def test_direccion_omite_campos_vacios():
    c = Cliente("1", "Ana", "a@x.com", "300", "NORMAL", ciudad="Manizales")
    assert c.direccion_completa() == "Manizales"
