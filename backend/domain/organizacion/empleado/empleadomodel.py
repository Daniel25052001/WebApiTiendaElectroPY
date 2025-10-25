
from pydantic import BaseModel

class EmpleadoModel(BaseModel):
    IdEmpleado: int
    Nombre: str
    Cargo: str
    IdSede: int
