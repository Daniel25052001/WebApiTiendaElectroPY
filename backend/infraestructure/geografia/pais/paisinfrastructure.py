import psycopg2
import psycopg2.extras
from domain.geografia.pais.paismodel import PaisModel

class PaisInfrastructure:

    @staticmethod
    def ingresar_pais(pais: PaisModel):
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarPais(%s);", (pais.nombre,))
                conn.commit()
                return {"mensaje": "País ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_pais(pais: PaisModel):
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT spaModificarPais(%s,%s,%s);",
                    (pais.idpais, pais.nombre, '1' if pais.activo else '0')
                )
                conn.commit()
                return {"mensaje": "País modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_pais(idpais: str):
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarPais(%s);", (idpais,))
                conn.commit()
                return {"mensaje": f"País {idpais} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_pais():
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarPais();")
                result = cur.fetchall()
                # Convertir nombres de columna a minúsculas para React
                result = [{k.lower(): v for k, v in row.items()} for row in result]
                return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_pais_por_id(idpais: str):
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarPaisPorId(%s);", (idpais,))
                result = cur.fetchone()
                if result:
                    # Convertir nombres de columna a minúsculas
                    result = {k.lower(): v for k, v in result.items()}
                    return result
                else:
                    return {"mensaje": "País no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
