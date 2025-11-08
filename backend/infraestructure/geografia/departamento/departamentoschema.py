from sqlalchemy import Table, Column, String, Boolean, ForeignKey, MetaData

meta = MetaData()

departamento = Table(
    "departamento", meta,
    Column("idDepartamento", String, primary_key=True),
    Column("nombre", String),
    Column("idDepartamento", String, ForeignKey("departamento.iddepartamento")),
    Column("activo", Boolean)
)
