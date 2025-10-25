from pydantic import BaseModel

class DepartamentoModel(BaseModel):
    iddepartamento: str
    nombre: str
    idpais: str
    activo: bool
