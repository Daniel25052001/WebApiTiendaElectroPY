
from pydantic import BaseModel 

class DetalleVentaModel(BaseModel):
    IdDetalle: int
    IdVenta: int
    IdProducto: int
    Cantidad: int
    PrecioUnitario: float
