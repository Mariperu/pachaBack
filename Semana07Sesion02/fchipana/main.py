from conexion import Conexion

class Mobile:
    def __init__(self, nombre, marca, modelo):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo

    def ToDic(self):
        return{
            "nombre":self.nombre,
            "marca":self.marca,
            "modelo":self.modelo
        }


conn = Conexion("mongodb://localhost:27017","Sesion2")

equipo = Mobile("Iphone", "Apple","14 pro")


#conn.insertar_registro("producto",equipo.ToDic())

#data = conn.obtener_registros("producto")
condicion = {
    'marca': 'Android'
}
newvalues = { "$set": { 'marca': "Android" } }
#data = conn.obtener_registro("producto",condicion)
#respuesta = conn.actualizar_registros("producto",condicion,newvalues)
respuesta = conn.borrar_registros("producto",condicion)
if(respuesta):
    print(f"Se actualizo correctamente")
else:
    print(f"No se actualizo")
#print(data)


conn.cerrar_conexion()