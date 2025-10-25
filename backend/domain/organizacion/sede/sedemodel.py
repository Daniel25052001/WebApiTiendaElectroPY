from pydantic import BaseModel

class SedeModel(BaseModel):
    idsede: str
    nombre: str
    direccion: str
    telefono: str
    idciudad: str
    activo: bool
