import os
import random
from faker import Faker
from tabulate import tabulate
from pymongo import MongoClient

# Establecer conexión con MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['hackaton06']  # Nombre de la base de datos

# Crear colecciones
alumnos_col = db['Alumnos']
salon_col = db['Salon']
cursos_col = db['Cursos']
profesores_col = db['Profesores']

def crear_colecciones():
    # Crear índices (opcional)
    alumnos_col.create_index('identificador', unique=True)
    salon_col.create_index('nombre', unique=True)
    cursos_col.create_index('nombre', unique=True)
    profesores_col.create_index('identificador', unique=True)

def limpiar_colecciones():
    # Eliminar todos los registros de la colección Alumnos
    alumnos_col.delete_many({})

    # Eliminar todos los registros de la colección Cursos
    cursos_col.delete_many({})

    # Eliminar todos los registros de la colección Profesores
    profesores_col.delete_many({})

    # Eliminar todos los registros de la colección Salon
    salon_col.delete_many({})

def cargar_registros_iniciales():
    fake = Faker()

    for i in range(1, 11):
        nombre = f"Salon {i}"
        año_escolar = str(random.randint(2022, 2023))
        salon_col.insert_one({"nombre": nombre, "año_escolar": año_escolar})

    # Obtener todos los documentos de la colección Salon
    salones = list(salon_col.find())

    # Cargar registros en la colección Alumnos
    for _ in range(20):
        alumno = {
            "identificador": fake.random_int(min=1, max=100),
            "nombre": fake.name(),
            "edad": fake.random_int(min=15, max=18),
            "correo": fake.email(),
            "salon_id": random.choice(salones)["_id"]
        }
        alumnos_col.insert_one(alumno)

    # Cargar registros en la colección Cursos
    for _ in range(20):
        curso = {
            "nombre": fake.word(),
            "profesor": fake.name(),
            "salon_id": random.choice(salones)["_id"]
        }
        cursos_col.insert_one(curso)

    # Obtener todos los documentos de la colección Profesores
    profesores = profesores_col.find()

    # Cargar registros en la colección Profesores
    for _ in range(20):
        profesor = {
            "identificador": fake.random_int(min=1, max=100),
            "nombre": fake.name(),
            "edad": fake.random_int(min=30, max=60),
            "correo": fake.email(),
            "salon_id": random.choice(salones)["_id"]
        }
        profesores_col.insert_one(profesor)


def agregar_registro(tabla):
    if tabla == "Alumnos":
        nombre = input("Ingrese el nombre del alumno: ")
        identificador = input("Ingrese el identificador del alumno: ")
        edad = input("Ingrese la edad del alumno: ")
        correo = input("Ingrese el correo del alumno: ")

        alumno = {
            "nombre": nombre,
            "identificador": identificador,
            "edad": edad,
            "correo": correo
        }

        alumnos_col.insert_one(alumno)
        print("Registro agregado con éxito.")

    elif tabla == "Salon":
        nombre = input("Ingrese el nombre del salón: ")
        anio_escolar = input("Ingrese el año escolar: ")

        salon = {
            "nombre": nombre,
            "anio_escolar": anio_escolar
        }

        salon_id = salon_col.insert_one(salon).inserted_id

        profesor = input("Ingrese el nombre del profesor asociado al salón: ")
        cursos = input("Ingrese los cursos asociados al salón (separados por comas): ")
        cursos = [curso.strip() for curso in cursos.split(",")]

        cursos_data = []
        for curso in cursos:
            curso_data = {
                "nombre": curso,
                "profesor": profesor,
                "salon_id": salon_id
            }
            cursos_data.append(curso_data)

        cursos_col.insert_many(cursos_data)
        print("Registro agregado con éxito.")

    elif tabla == "Cursos":
        nombre = input("Ingrese el nombre del curso: ")
        profesor = input("Ingrese el nombre del profesor a cargo: ")

        curso = {
            "nombre": nombre,
            "profesor": profesor
        }

        cursos_col.insert_one(curso)
        print("Registro agregado con éxito.")

    elif tabla == "Profesores":
        nombre = input("Ingrese el nombre del profesor: ")
        identificador = input("Ingrese el identificador del profesor: ")
        edad = input("Ingrese la edad del profesor: ")
        correo = input("Ingrese el correo del profesor: ")

        profesor = {
            "nombre": nombre,
            "identificador": identificador,
            "edad": edad,
            "correo": correo
        }

        profesores_col.insert_one(profesor)
        print("Registro agregado con éxito.")


def modificar_registro(tabla):
    if tabla == "Alumnos":
        identificador = input("Ingrese el identificador del alumno a modificar: ")

        alumno = alumnos_col.find_one({"identificador": identificador})

        if alumno:
            print("Datos actuales del alumno:")
            print(alumno)

            nombre = input("Ingrese el nuevo nombre del alumno: ")
            edad = input("Ingrese la nueva edad del alumno: ")
            correo = input("Ingrese el nuevo correo del alumno: ")

            nuevos_datos = {
                "$set": {
                    "nombre": nombre,
                    "edad": edad,
                    "correo": correo
                }
            }

            alumnos_col.update_one({"identificador": identificador}, nuevos_datos)
            print("Registro modificado con éxito.")
        else:
            print("No se encontró ningún alumno con ese identificador.")

    elif tabla == "Salon":
        nombre = input("Ingrese el nombre del salón a modificar: ")

        salon = salon_col.find_one({"nombre": nombre})

        if salon:
            print("Datos actuales del salón:")
            print(salon)

            nuevo_nombre = input("Ingrese el nuevo nombre del salón: ")
            nuevo_anio = input("Ingrese el nuevo año escolar: ")

            nuevos_datos = {
                "$set": {
                    "nombre": nuevo_nombre,
                    "anio_escolar": nuevo_anio
                }
            }

            salon_col.update_one({"nombre": nombre}, nuevos_datos)
            print("Registro modificado con éxito.")
        else:
            print("No se encontró ningún salón con ese nombre.")

    elif tabla == "Cursos":
        nombre = input("Ingrese el nombre del curso a modificar: ")

        curso = cursos_col.find_one({"nombre": nombre})

        if curso:
            print("Datos actuales del curso:")
            print(curso)

            nuevo_nombre = input("Ingrese el nuevo nombre del curso: ")
            nuevo_profesor = input("Ingrese el nuevo nombre del profesor a cargo: ")

            nuevos_datos = {
                "$set": {
                    "nombre": nuevo_nombre,
                    "profesor": nuevo_profesor
                }
            }

            cursos_col.update_one({"nombre": nombre}, nuevos_datos)
            print("Registro modificado con éxito.")
        else:
            print("No se encontró ningún curso con ese nombre.")

    elif tabla == "Profesores":
        identificador = input("Ingrese el identificador del profesor a modificar: ")

        profesor = profesores_col.find_one({"identificador": identificador})

        if profesor:
            print("Datos actuales del profesor:")
            print(profesor)

            nombre = input("Ingrese el nuevo nombre del profesor: ")
            edad = input("Ingrese la nueva edad del profesor: ")
            correo = input("Ingrese el nuevo correo del profesor: ")

            nuevos_datos = {
                "$set": {
                    "nombre": nombre,
                    "edad": edad,
                    "correo": correo
                }
            }

            profesores_col.update_one({"identificador": identificador}, nuevos_datos)
            print("Registro modificado con éxito.")
        else:
            print("No se encontró ningún profesor con ese identificador.")


def eliminar_registro(tabla):
    if tabla == "Alumnos":
        identificador = input("Ingrese el identificador del alumno a eliminar: ")

        alumno = alumnos_col.find_one({"identificador": identificador})

        if alumno:
            confirmacion = input("¿Está seguro de que desea eliminar este alumno? (s/n): ")

            if confirmacion.lower() == "s":
                alumnos_col.delete_one({"identificador": identificador})
                print("Alumno eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró ningún alumno con ese identificador.")

    elif tabla == "Salon":
        nombre = input("Ingrese el nombre del salón a eliminar: ")

        salon = salon_col.find_one({"nombre": nombre})

        if salon:
            confirmacion = input("¿Está seguro de que desea eliminar este salón? (s/n): ")

            if confirmacion.lower() == "s":
                salon_col.delete_one({"nombre": nombre})
                print("Salón eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró ningún salón con ese nombre.")

    elif tabla == "Cursos":
        nombre = input("Ingrese el nombre del curso a eliminar: ")

        curso = cursos_col.find_one({"nombre": nombre})

        if curso:
            confirmacion = input("¿Está seguro de que desea eliminar este curso? (s/n): ")

            if confirmacion.lower() == "s":
                cursos_col.delete_one({"nombre": nombre})
                print("Curso eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró ningún curso con ese nombre.")

    elif tabla == "Profesores":
        identificador = input("Ingrese el identificador del profesor a eliminar: ")

        profesor = profesores_col.find_one({"identificador": identificador})

        if profesor:
            confirmacion = input("¿Está seguro de que desea eliminar este profesor? (s/n): ")

            if confirmacion.lower() == "s":
                profesores_col.delete_one({"identificador": identificador})
                print("Profesor eliminado con éxito.")
            else:
                print("Eliminación cancelada.")
        else:
            print("No se encontró ningún profesor con ese identificador.")


def consultar_registros(tabla):
    if tabla == "Alumnos":
        print("Listado de Alumnos:")
        alumnos = alumnos_col.find()

        registros = []
        for alumno in alumnos:
            registro = [alumno["identificador"], alumno["nombre"], alumno["edad"], alumno["correo"]]
            registros.append(registro)

        headers = ["Identificador", "Nombre", "Edad", "Correo"]
        print(tabulate(registros, headers, tablefmt="grid"))

    elif tabla == "Salon":
        print("Listado de Salones:")
        salones = salon_col.find()

        registros = []
        for salon in salones:
            registro = [salon["nombre"], salon["anio_escolar"]]
            registros.append(registro)

        headers = ["Nombre", "Año Escolar"]
        print(tabulate(registros, headers, tablefmt="grid"))

    elif tabla == "Cursos":
        print("Listado de Cursos:")
        cursos = cursos_col.find()

        registros = []
        for curso in cursos:
            registro = [curso["nombre"], curso["profesor"]]
            registros.append(registro)

        headers = ["Nombre", "Profesor"]
        print(tabulate(registros, headers, tablefmt="grid"))

    elif tabla == "Profesores":
        print("Listado de Profesores:")
        profesores = profesores_col.find()

        registros = []
        for profesor in profesores:
            registro = [profesor["identificador"], profesor["nombre"], profesor["edad"], profesor["correo"]]
            registros.append(registro)

        headers = ["Identificador", "Nombre", "Edad", "Correo"]
        print(tabulate(registros, headers, tablefmt="grid"))


def menu_tabla(tabla):
    while True:
        # limpiarPantalla()
        print(f"--- Menú de Transacciones ( {tabla} ) ---")
        print("")
        print("1. Agregar registro")
        print("2. Modificar registro")
        print("3. Eliminar registro")
        print("4. Mostrar registros")
        print("0. Salir")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            mantener_sec = agregar_registro(tabla)
            if mantener_sec == False:
                break
        elif opcion == "2":
            mantener_sec = modificar_registro(tabla)
            if mantener_sec == False:
                break
        elif opcion == "3":
            mantener_sec = eliminar_registro(tabla)
            if mantener_sec == False:
                break
        elif opcion == "4":
            mantener_sec = consultar_registros(tabla)
            if mantener_sec == False:
                break
        elif opcion == "0":
            break
        else:
            print("\nOpción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    # Conexión y manipulacion de la base de datos PostgreSQL
    # conn,cursor = conectar_db()
    
    # crear_tablas()
    # agregar_relaciones()

    # while True:
    #     limpiarPantalla()
    #     restablecer = input("Se programo un restablecimiento de registros iniciales, desea omitirlo? (Y/N):\n")
    #     if restablecer.upper() == "N":
    #         borrar_registros()
    #         restablecer_id("Alumnos")
    #         restablecer_id("Profesores")
    #         restablecer_id("Cursos")
    #         restablecer_id("Salon")
    #         break
    #     elif restablecer.upper() == "Y":
    #         break
    #     else:
    #         print("\nOpción inválida. Intente nuevamente.\n")

    # cargar_registros_fijos()
    
    limpiar_colecciones()
    cargar_registros_iniciales()


    # Menú principal

    while True:
        # limpiarPantalla()
        print("--- Menú principal ---")
        print("")
        print("1. Alumnos")
        print("2. Salón")
        print("3. Cursos")
        print("4. Profesores")
        print("0. Salir")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            menu_tabla("Alumnos")
        elif opcion == "2":
            menu_tabla("Salon")
        elif opcion == "3":
            menu_tabla("Cursos")
        elif opcion == "4":
            menu_tabla("Profesores")
        elif opcion == "0":
            break
        else:
            print("\nOpción inválida. Intente nuevamente.\n")

    # limpiarPantalla()

    print("Fin del programa.")


def limpiarPantalla():
    def clear():
        return os.system('cls')
        #return os.system('clear')
    clear() 