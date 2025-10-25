from pydantic import BaseModel

class CiudadModel(BaseModel):
    idciudad: str
    nombre: str
    iddepartamento: str
    activo: bool
