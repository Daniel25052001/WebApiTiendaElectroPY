
from pydantic import BaseModel


class TipoDocumentoModel(BaseModel):
    IdTipoDocumento: int
    Nombre: str
    Abreviatura: str
