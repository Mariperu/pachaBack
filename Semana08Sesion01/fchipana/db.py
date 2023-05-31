import psycopg2
from psycopg2 import Error

class db:
    def conexion(self):
        try:
            conn = psycopg2.connect(user='postgres',
                                    password="Zal20059",
                                    host="localhost",
                                    port="5432",
                                    database="biblioteca")
            return conn
        except Error as error:
            print(f"Ha ocurrido en error: {str(error)}")
            return False
        
    def consultarBDD(self, query): 
        try:    
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            records = cur.fetchall()
            return records
        except Error as error:
            print(f"Ha ocurrido un error: {str(error)}")
            return False
        finally:
            if(conexion):
                cur.close()
                conexion.close()
    def ejecutarBDD(self, query):
        try:
            conexion = self.conexion()
            cur = conexion.cursor()
            cur.execute(query)
            conexion.commit()
            exito = True
            return exito
        except Error as error:
            print(f"Ha ocurrido un error: {str(error)}")
            input("Desea Continuar")
            return False
        finally:
            if(conexion):
                cur.close()
                conexion.close()