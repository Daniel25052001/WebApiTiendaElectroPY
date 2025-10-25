import psycopg2
import psycopg2.extras
from domain.producto.producto.ProductoModel import ProductoModel

class ProductoInfrastructure:

    @staticmethod
    def ingresar_producto(prod: ProductoModel):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarProducto(%s,%s,%s,%s);",
                            (prod.nombre, prod.descripcion, prod.precio, prod.stock))
                conn.commit()
                return {"mensaje": "Producto ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_producto(prod: ProductoModel):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarProducto(%s,%s,%s,%s,%s,%s);",
                            (prod.idproducto, prod.nombre, prod.descripcion,
                             prod.precio, prod.stock, '1' if prod.activo else '0'))
                conn.commit()
                return {"mensaje": "Producto modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_producto(idproducto: str):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarProducto(%s);", (idproducto,))
                conn.commit()
                return {"mensaje": f"Producto {idproducto} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_producto():
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarProducto();")
                result = cur.fetchall()
                return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_producto_por_id(idproducto: str):
        try:
            conn = psycopg2.connect(dbname='dbatiendaelectro', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarProductoPorId(%s);", (idproducto,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Producto no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()
