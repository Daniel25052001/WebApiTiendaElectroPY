
from pydantic import BaseModel

class EstadoDeVentaModel(BaseModel):
    IdEstado: int
    Nombre: str
