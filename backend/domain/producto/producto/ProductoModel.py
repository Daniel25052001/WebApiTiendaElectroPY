from pydantic import BaseModel

class ProductoModel(BaseModel):
    idproducto: str
    nombre: str
    descripcion: str
    precio: float
    stock: int
    activo: bool
