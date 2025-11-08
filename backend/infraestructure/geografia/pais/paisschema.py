
from sqlalchemy import Table, Column, String, Boolean, ForeignKey, MetaData

meta = MetaData()

pais = Table(
    "Pais", meta,
    Column("idPais", String, primary_key=True),
    Column("nombre", String),
    Column("idPais", String, ForeignKey("pais.idPais")),
    Column("activo", Boolean)
)
