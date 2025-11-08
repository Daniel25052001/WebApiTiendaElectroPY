import psycopg2
import psycopg2.extras
from domain.geografia.departamento.departamentomodel import DepartamentoModel

class DepartamentoInfrastructure:

    @staticmethod
    def ingresar_departamento(dep: DepartamentoModel):
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarDepartamento(%s,%s);", (dep.nombre, dep.idpais))
                conn.commit()
                return {"mensaje": "Departamento ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_departamento(dep: DepartamentoModel):
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
                    "SELECT spaModificarDepartamento(%s,%s,%s,%s);",
                    (dep.iddepartamento, dep.nombre, dep.idpais, '1' if dep.activo else '0')
                )
                conn.commit()
                return {"mensaje": "Departamento modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_departamento(iddepartamento: str):
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarDepartamento(%s);", (iddepartamento,))
                conn.commit()
                return {"mensaje": f"Departamento {iddepartamento} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_departamento():
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarDepartamento();")
                result = cur.fetchall()
                # Convertir las claves a minúsculas para React
                result = [{k.lower(): v for k, v in row.items()} for row in result]
                return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_departamento_por_id(iddepartamento: str):
        try:
            conn = psycopg2.connect(
                dbname='dbatiendaelectro', 
                user='postgres',
                password='', 
                host='127.0.0.1', 
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarDepartamentoPorId(%s);", (iddepartamento,))
                result = cur.fetchone()
                if result:
                    # Convertir claves a minúsculas para React
                    result = {k.lower(): v for k, v in result.items()}
                    return result
                else:
                    return {"mensaje": "Departamento no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
