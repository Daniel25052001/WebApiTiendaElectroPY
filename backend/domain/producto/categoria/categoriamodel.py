
from pydantic import BaseModel

class CategoriaModel(BaseModel):
    IdCategoria: int
    Nombre: str
    