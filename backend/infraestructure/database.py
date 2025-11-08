
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Cambia por tus datos reales de PostgreSQL
DATABASE_URL = "postgresql://postgres:tu_contraseña@localhost:5432/tiendaelectro"

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
