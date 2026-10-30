from dataclasses import dataclass

@dataclass
class Cliente:
    documento: str
    nombre: str
    email: str
    telefono: str
    tipo: str
    calle: str = ""
    ciudad: str = ""
    departamento: str = ""
    codigo_postal: str = ""

    def direccion_completa(self) -> str:
        partes = [self.calle.strip(), self.ciudad.strip(),
                  self.departamento.strip(), self.codigo_postal.strip()]
        return ", ".join(p for p in partes if p)
