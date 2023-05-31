from pymongo import MongoClient

class Conexion:
    def __init__(self, uri, database):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[database]
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")

    def insertar_registro(self, collection, data):
        try:
            collection = self.db[collection]
            result = collection.insert_one(data)
            print(f"Registros insertados: {result.inserted_id}")
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")

    def obtener_registros(self, collection, condition={}):
        try:
            collection = self.db[collection]
            data = collection.find(condition)
            return list(data)
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")
    
    def obtener_registro(self, collection, condition={}):
        try:
            collection = self.db[collection]
            data = collection.find_one(condition)
            return list(data)
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")

    def actualizar_registro(self, collection, condition={}, newValues={}):
        try:
            collection = self.db[collection]
            result = collection.update_one(condition, newValues)
            return True
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")
            return False
        
    def actualizar_registros(self, collection, condition={}, newValues={}):
        try:
            collection = self.db[collection]
            result = collection.update_many(condition, newValues)
            return True
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")
            return False
        
    def borrar_registro(self, collection, condition={}):
        try:
            collection = self.db[collection]
            result = collection.delete_one(condition)
            return True
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")
            return False   
             
    def borrar_registros(self, collection, condition={}):
        try:
            collection = self.db[collection]
            result = collection.delete_many(condition)
            return True
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")
            return False        

    def cerrar_conexion(self):
        try:
            self.db.close()
            print("Esta conexion se ha cerrado correctamente")
        except Exception as error:
            print(f"Ha ocurrido un error: {error}")


    