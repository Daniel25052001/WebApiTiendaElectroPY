import psycopg2
import psycopg2.extras
from domain.geografia.ciudad.ciudadmodel import CiudadModel

class CiudadInfrastructure:

    @staticmethod
    def ingresar_ciudad(ciudad: CiudadModel):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarCiudad(%s,%s);",
                            (ciudad.nombre, ciudad.iddepartamento))
                conn.commit()
                return {"mensaje": "Ciudad ingresada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_ciudad(ciudad: CiudadModel):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarCiudad(%s,%s,%s,%s);",
                            (ciudad.idciudad, ciudad.nombre, ciudad.iddepartamento,
                             '1' if ciudad.activo else '0'))
                conn.commit()
                return {"mensaje": "Ciudad modificada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_ciudad(idciudad: str):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarCiudad(%s);", (idciudad,))
                conn.commit()
                return {"mensaje": f"Ciudad {idciudad} eliminada físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_ciudad():
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCiudad();")
                result = cur.fetchall()
                return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_ciudad_por_id(idciudad: str):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarCiudadPorId(%s);", (idciudad,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Ciudad no encontrada"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
