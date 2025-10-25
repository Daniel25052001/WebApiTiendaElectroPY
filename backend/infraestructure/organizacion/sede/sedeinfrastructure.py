import psycopg2
import psycopg2.extras
from domain.organizacion.sede.sedemodel import SedeModel

class SedeInfrastructure:

    @staticmethod
    def ingresar_sede(sede: SedeModel):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarSede(%s,%s,%s,%s);",
                            (sede.nombre, sede.direccion, sede.telefono, sede.idciudad))
                conn.commit()
                return {"mensaje": "Sede ingresada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_sede(sede: SedeModel):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarSede(%s,%s,%s,%s,%s,%s);",
                            (sede.idsede, sede.nombre, sede.direccion, sede.telefono,
                             sede.idciudad, '1' if sede.activo else '0'))
                conn.commit()
                return {"mensaje": "Sede modificada correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_sede(idsede: str):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarSede(%s);", (idsede,))
                conn.commit()
                return {"mensaje": f"Sede {idsede} eliminada físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_sede():
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarSede();")
                result = cur.fetchall()
                return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_sede_por_id(idsede: str):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarSedePorId(%s);", (idsede,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Sede no encontrada"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
