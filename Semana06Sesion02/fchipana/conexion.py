import psycopg2
from psycopg2 import Error

class conexion:
    def conexion(self):
        try:
            conn = psycopg2.connect(user='postgres',
                                    password="pacha23",
                                    host="localhost",
                                    port="5432",
                                    database="D19423")
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
            return False
        finally:
            if(conexion):
                cur.close()
                conexion.close()


# from conexion import conexion
# from tabulate import TableFormat,tabulate

# conexion = conexion()
# query = "Select * from clientes;"
# datos = conexion.consultarBDD(query)
# header = ["ID","Nombre","IdSegmento","IdPais","IdCiudad","IdEstado","Codigo Postal","IdRegion"]

# print(tabulate(datos,headers=header,tablefmt="fancy_grid"))

# nombre = input("Dime tu nombre: ")
# idsegmento = int(input("Dime tu segmento: "))
# idpais = int(input("Dime tu idpais: "))
# idciudad = int(input("Dime tu idCiudad: "))
# idestado = int(input("Dime tu idEstado: "))
# codigopostal = int(input("Dime tu codigo postal: "))
# idregion = int(input("Dime tu idRegion: "))

# query= f'''insert into clientes(nombrecliente,idsegmento,idpais,idciudad,idestado,codigopostal,idregion)
# values('{nombre}',{idsegmento},{idpais},{idciudad},{idestado},'{codigopostal}',{idregion});'''
# print(query)
# if(conexion.)