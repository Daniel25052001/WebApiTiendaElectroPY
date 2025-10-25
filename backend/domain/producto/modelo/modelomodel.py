
from pydantic import BaseModel

class ModeloModel(BaseModel):
    IdModelo: int
    Nombre: str
    IdMarca: int
    IdCategoria: int
