from typing import Optional
from pydantic import BaseModel, Field


class CiudadModel(BaseModel):
    idciudad: Optional[str] = None
    nombre: str
    iddepartamento: str
    activo: bool = Field(default=True)
