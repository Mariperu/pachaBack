import psycopg2
import os
import random
from tabulate import tabulate
from clase import conectar_db


# FUNCIONES PARA INTERACTUAR CON BASE DE DATOS POSTGRESS PT70823995

def restablecer_id(tabla):

    # Restablecer los ID de las tablas

    conn,cursor = conectar_db()

    cursor.execute(f"ALTER SEQUENCE {tabla}_id_seq RESTART WITH 1")

    conn.commit()

    cursor.close()
    conn.close()

def crear_tablas():

    conn,cursor = conectar_db()

    # Tabla Alumnos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alumnos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            identificador VARCHAR(10),
            edad INTEGER,
            correo VARCHAR(100)
        );
    """)

    # Tabla Salon
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Salon (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            año_escolar VARCHAR(20)
        );
    """)

    # Tabla Cursos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cursos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            profesor VARCHAR(100),
            salon_id INTEGER REFERENCES Salon(id)
        );
    """)

    # Tabla Profesores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Profesores (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            identificador VARCHAR(10),
            edad INTEGER,
            correo VARCHAR(100),
            salon_id INTEGER REFERENCES Salon(id)
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

def agregar_relaciones():

#FK
    conn,cursor = conectar_db()

    cursor.execute("""
        ALTER TABLE Alumnos
        ADD COLUMN IF NOT EXISTS salon_id INTEGER REFERENCES Salon(id);
    """)

    cursor.execute("""
        ALTER TABLE Profesores
        ADD COLUMN IF NOT EXISTS salon_id INTEGER REFERENCES Salon(id);
    """)

    cursor.execute("""
        ALTER TABLE Cursos
        ADD COLUMN IF NOT EXISTS salon_id INTEGER REFERENCES Salon(id);
    """)

    conn.commit()
    cursor.close()
    conn.close()

def borrar_registros():

    conn,cursor = conectar_db()

    cursor.execute("DELETE FROM Alumnos")
    cursor.execute("DELETE FROM Profesores")
    cursor.execute("DELETE FROM Cursos")
    cursor.execute("DELETE FROM Salon")

    conn.commit()

    cursor.close()
    conn.close()

def cargar_registros_fijos():

    conn,cursor = conectar_db()

    for i in range(5):
        nombre = f"Salon{i}"
        año_escolar = random.randint(2022, 2023)
        cursor.execute("INSERT INTO Salon (nombre, año_escolar) VALUES (%s, %s) RETURNING id",
                       (nombre, año_escolar))
        row = cursor.fetchone()
        if row is not None:
            salon_id = row[0]

            # Cargar registros fijos
            for j in range(1):
                nombre_alumno = f"Alumno{j}"
                identificador_alumno = f"AL-{j}"
                edad_alumno = random.randint(14, 18)
                correo_alumno = f"alumno{j}@example.com"
                cursor.execute("INSERT INTO Alumnos (nombre, identificador, edad, correo, salon_id) VALUES (%s, %s, %s, %s, %s)",
                               (nombre_alumno, identificador_alumno, edad_alumno, correo_alumno, salon_id))

                nombre_profesor = f"Profesor{j}"
                identificador_profesor = f"PR-{j}"
                edad_profesor = random.randint(30, 50)
                correo_profesor = f"profesor{j}@example.com"
                cursor.execute("INSERT INTO Profesores (nombre, identificador, edad, correo, salon_id) VALUES (%s, %s, %s, %s, %s)",
                               (nombre_profesor, identificador_profesor, edad_profesor, correo_profesor, salon_id))

                nombre_curso = f"Curso{j}"
                cursor.execute("INSERT INTO Cursos (nombre, profesor, salon_id) VALUES (%s, %s, %s)",
                               (nombre_curso, nombre_profesor, salon_id))

    conn.commit()

    cursor.close()
    conn.close()

def menu_tabla(tabla):
    while True:
        limpiarPantalla()
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
        

# Funciones para manipular los registros de cada tabla

def limpiarPantalla():
    def clear():
        return os.system('cls')
        #return os.system('clear')
    clear() 

def agregar_registro(tabla):

    limpiarPantalla()

    conn,cursor = conectar_db()

    if tabla == "Alumnos":
        nombre = input("Ingrese el nombre del alumno: ")
        identificador = input("Ingrese el identificador del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        correo = input("Ingrese el correo del alumno: ")
        salon_id = int(input("Ingrese el ID del salón al que pertenece el alumno: "))

        cursor.execute("""
            INSERT INTO Alumnos (nombre, identificador, edad, correo, salon_id)
            VALUES (%s, %s, %s, %s, %s);
        """, (nombre, identificador, edad, correo, salon_id))

    elif tabla == "Salon":
        nombre = input("Ingrese el nombre del salón: ")
        año_escolar = input("Ingrese el año escolar del salón: ")

        cursor.execute("""
            INSERT INTO Salon (nombre, año_escolar)
            VALUES (%s, %s);
        """, (nombre, año_escolar))

    elif tabla == "Cursos":
        nombre = input("Ingrese el nombre del curso: ")
        profesor = input("Ingrese el nombre del profesor del curso: ")
        salon_id = int(input("Ingrese el ID del salón al que pertenece el curso: "))

        cursor.execute("""
            INSERT INTO Cursos (nombre, profesor, salon_id)
            VALUES (%s, %s, %s);
        """, (nombre, profesor, salon_id))

    elif tabla == "Profesores":
        nombre = input("Ingrese el nombre del profesor: ")
        identificador = input("Ingrese el identificador del profesor: ")
        edad = int(input("Ingrese la edad del profesor: "))
        correo = input("Ingrese el correo del profesor: ")
        salon_id = int(input("Ingrese el ID del salón al que está asociado el profesor: "))

        cursor.execute("""
            INSERT INTO Profesores (nombre, identificador, edad, correo, salon_id)
            VALUES (%s, %s, %s, %s, %s);
        """, (nombre, identificador, edad, correo, salon_id))

    conn.commit()
    cursor.close()
    conn.close()

    while True:
        consulta_retorno_menu_01 = input("Desea realizar alguna otra transaccion en el menu de transacciones? (Y/N): \n")
        if consulta_retorno_menu_01.upper() == "Y":
            return True
        elif consulta_retorno_menu_01.upper() == "N":
            return False
        else:
            print("\nOpción inválida. Intente nuevamente.\n")

def modificar_registro(tabla):
    limpiarPantalla()

    conn,cursor = conectar_db()

    if tabla == "Alumnos":
        alumno_id = int(input("Ingrese el ID del alumno que desea modificar: "))
        nombre = input("Ingrese el nuevo nombre del alumno: ")
        identificador = input("Ingrese el nuevo identificador del alumno: ")
        edad = int(input("Ingrese la nueva edad del alumno: "))
        correo = input("Ingrese el nuevo correo del alumno: ")
        salon_id = int(input("Ingrese el nuevo ID del salón al que pertenece el alumno: "))

        cursor.execute("""
            UPDATE Alumnos
            SET nombre = %s, identificador = %s, edad = %s, correo = %s, salon_id = %s
            WHERE id = %s;
        """, (nombre, identificador, edad, correo, salon_id, alumno_id))

    elif tabla == "Salon":
        salon_id = int(input("Ingrese el ID del salón que desea modificar: "))
        nombre = input("Ingrese el nuevo nombre del salón: ")
        año_escolar = input("Ingrese el nuevo año escolar del salón: ")

        cursor.execute("""
            UPDATE Salon
            SET nombre = %s, año_escolar = %s
            WHERE id = %s;
        """, (nombre, año_escolar, salon_id))

    elif tabla == "Cursos":
        curso_id = int(input("Ingrese el ID del curso que desea modificar: "))
        nombre = input("Ingrese el nuevo nombre del curso: ")
        profesor = input("Ingrese el nuevo nombre del profesor del curso: ")
        salon_id = int(input("Ingrese el nuevo ID del salón al que pertenece el curso: "))

        cursor.execute("""
            UPDATE Cursos
            SET nombre = %s, profesor = %s, salon_id = %s
            WHERE id = %s;
        """, (nombre, profesor, salon_id, curso_id))

    elif tabla == "Profesores":
        profesor_id = int(input("Ingrese el ID del profesor que desea modificar: "))
        nombre = input("Ingrese el nuevo nombre del profesor: ")
        identificador = input("Ingrese el nuevo identificador del profesor: ")
        edad = int(input("Ingrese la nueva edad del profesor: "))
        correo = input("Ingrese el nuevo correo del profesor: ")
        salon_id = int(input("Ingrese el nuevo ID del salón al que está asociado el profesor: "))

        cursor.execute("""
            UPDATE Profesores
            SET nombre = %s, identificador = %s, edad = %s, correo = %s, salon_id = %s
            WHERE id = %s;
        """, (nombre, identificador, edad, correo, salon_id, profesor_id))

    conn.commit()
    cursor.close()
    conn.close()

    while True:
        consulta_retorno_menu_01 = input("Desea realizar alguna otra transaccion en el menu de transacciones? (Y/N): \n")
        if consulta_retorno_menu_01.upper() == "Y":
            return True
        elif consulta_retorno_menu_01.upper() == "N":
            return False
        else:
            print("\nOpción inválida. Intente nuevamente.\n")

def eliminar_registro(tabla):

    limpiarPantalla()

    conn,cursor = conectar_db()

    if tabla == "Alumnos":
        alumno_id = int(input("Ingrese el ID del alumno que desea eliminar: "))

        cursor.execute("""
            DELETE FROM Alumnos
            WHERE id = %s;
        """, (alumno_id,))

    elif tabla == "Salon":
        salon_id = int(input("Ingrese el ID del salón que desea eliminar: "))

        cursor.execute("""
            DELETE FROM Salon
            WHERE id = %s;
        """, (salon_id,))

    elif tabla == "Cursos":
        curso_id = int(input("Ingrese el ID del curso que desea eliminar: "))

        cursor.execute("""
            DELETE FROM Cursos
            WHERE id = %s;
        """, (curso_id,))

    elif tabla == "Profesores":
        profesor_id = int(input("Ingrese el ID del profesor que desea eliminar: "))

        cursor.execute("""
            DELETE FROM Profesores
            WHERE id = %s;
        """, (profesor_id,))

    conn.commit()
    cursor.close()
    conn.close()

    while True:
        consulta_retorno_menu_01 = input("Desea realizar alguna otra transaccion en el menu de transacciones? (Y/N): \n")
        if consulta_retorno_menu_01.upper() == "Y":
            return True
        elif consulta_retorno_menu_01.upper() == "N":
            return False
        else:
            print("\nOpción inválida. Intente nuevamente.\n")

def consultar_registros(tabla):

    limpiarPantalla()

    print(f"\nEstos son los registros almacenados en la tabla {tabla} :\n")

    conn,cursor = conectar_db()

    headers = [] 
    rows = []

    if tabla == "Alumnos":
        cursor.execute("SELECT * FROM Alumnos;")
        registros = cursor.fetchall()

        headers = ["ID", "Nombre", "Identificador", "Edad", "Correo", "Salón ID"]
        rows = [[registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]] for registro in registros]

    elif tabla == "Salon":
        cursor.execute("SELECT * FROM Salon;")
        registros = cursor.fetchall()

        headers = ["ID", "Nombre", "Año Escolar"]
        rows = [[registro[0], registro[1], registro[2]] for registro in registros]

    elif tabla == "Cursos":
        cursor.execute("SELECT * FROM Cursos;")
        registros = cursor.fetchall()

        headers = ["ID", "Nombre", "Profesor", "Salón ID"]
        rows = [[registro[0], registro[1], registro[2], registro[3]] for registro in registros]
    

    elif tabla == "Profesores":
        cursor.execute("SELECT * FROM Profesores;")
        registros = cursor.fetchall()

        headers = ["ID", "Nombre", "Identificador", "Edad", "Correo", "Salón ID"]
        rows = [[registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]] for registro in registros]
    
    print(tabulate(rows, headers, tablefmt="grid"))

    cursor.close()
    conn.close()

    while True:
        consulta_retorno_menu_01 = input("Desea realizar alguna otra transaccion en el menu de transacciones? (Y/N): \n")
        if consulta_retorno_menu_01.upper() == "Y":
            return True
        elif consulta_retorno_menu_01.upper() == "N":
            return False
        else:
            print("\nOpción inválida. Intente nuevamente.\n")
    

# Ejecucion del programa base

if __name__ == "__main__":
    # Conexión y manipulacion de la base de datos PostgreSQL
    conn,cursor = conectar_db()
    
    crear_tablas()
    agregar_relaciones()

    while True:
        limpiarPantalla()
        restablecer = input("Se programo un restablecimiento de registros iniciales, desea omitirlo? (Y/N):\n")
        if restablecer.upper() == "N":
            borrar_registros()
            restablecer_id("Alumnos")
            restablecer_id("Profesores")
            restablecer_id("Cursos")
            restablecer_id("Salon")
            break
        elif restablecer.upper() == "Y":
            break
        else:
            print("\nOpción inválida. Intente nuevamente.\n")

    cargar_registros_fijos()
    
    # Menú principal

    while True:
        limpiarPantalla()
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

    conn.close()

    limpiarPantalla()

    print("Fin del programa.")

