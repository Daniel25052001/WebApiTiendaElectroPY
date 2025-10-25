
from pydantic import BaseModel

class FechaModel(BaseModel):
    IdFecha: int
    Fecha: str  # o datetime 
