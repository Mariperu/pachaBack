# from psycopg2 import connect, Error

# try:
#     conn = connect(
#         user = 'postgres', 
#         password = 'Zal20059', 
#         host='127.0.0.1', 
#         port = '5432', 
#         database = 'postgres')
#     cur = conn.cursor()
#     query = 'select version();'
#     cur.execute(query)
#     res = cur.fetchone()
#     print(res)

# except(Exception, Error) as error:
#     print(f"Hubo un error en la conexion {str(error)}")
# finally:
#     cur.close()
#     conn.close()
#     print(f'Se ha cerrado la conexion')

##########################################################################

# from conexion import conexion
# from tabulate import TableFormat, tabulate

# conexion = conexion()
# query = "Select * from clientes;"
# datos = conexion.consultarBDD(query)
# header = ['ID','Nombre','IdSegmento','IdPais','IdCiudad', 'IdEstado', 'Codigo postal', 'IdRegion']
# # print(tabulate(datos, headers=header, tablefmt='fancy_grid'))
# # print(datos)
# nombre = input("Dime tu nombre: ")
# idsegmento = int(input("Dime tu segmento"))
# idpais = int(input("Dime tu idpais: "))
# idciudad = int(input("Dime tu idCiudad: "))
# idestado = int(input("Dime tu idestado: "))
# codigopostal = input("Dime tu codigo postal: ")
# idregion = int(input("Dime tu idregion: "))

# query= f'''insert into clientes(nombrecliente,idsegmento,idpais,idciudad,idestado,codigopostal,idregion)
# values('{nombre}',{idsegmento},{idpais},{idciudad},{idestado},'{codigopostal}',{idregion});'''
# print(query)
# if(conexion.ejecutarBDD(query)):
#     print("Datos guardados correctamente")

# #Conector ODBC es para conectars ea cualquier base de datos

from utils import Menu
from clientes import Clientes
from conexion import conexion

lstClientes = []

def cargaInicial():
    res = conexion.consultarBDD("Select * from Clientes;")
    for cli in res:
        cliente = Clientes(cli.IdCliente,cli.NombreCliente,cli.IdSegmento,cli.IdPais,cli.IdCiudad,cli.IdEstado,cli.CodigoPostal,cli.IdRegion)
        lstClientes.append(cliente)


menu = Menu("Menu de Clientes")