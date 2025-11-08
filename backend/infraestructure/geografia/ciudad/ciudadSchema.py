
from sqlalchemy import Table, Column, String, Boolean, ForeignKey, MetaData

meta = MetaData()

ciudad = Table(
    "ciudad", meta,
    Column("idciudad", String, primary_key=True),
    Column("nombre", String),
    Column("iddepartamento", String, ForeignKey("departamento.iddepartamento")),
    Column("activo", Boolean)
)
