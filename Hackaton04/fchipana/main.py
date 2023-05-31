import os
import time
import json

class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

class Alumno(Persona):
    def __init__(self, nombre, dni, edad, curso, notas=None):
        super().__init__(nombre, dni, edad)
        self.curso = curso
        self.notas = notas or []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio_notas(self):
        return sum(self.notas) / len(self.notas)

    def reporte(self):
        promedio = self.promedio_notas()
        nota_maxima = max(self.notas)
        nota_minima = min(self.notas)

        reporte = f"Alumno: {self.nombre}, máxima nota: {nota_maxima}, mínima nota: {nota_minima}, promedio: {promedio}"
        return reporte

def registrar_alumnos():
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    curso = input("Ingrese el curso del alumno: ")

    alumno = Alumno(nombre, dni, edad, curso)

    o = True

    while o:
        print(f"Esta seguro que desea agregar al alumno {nombre} a lista de alumnos? (Y/N)")
        rpta = input("Respuesta: ")
        if(rpta.upper() =="Y"):
            with open("alumnos.txt", "a") as jsonfile:
                json.dump(alumno.__dict__, jsonfile)
                jsonfile.write("\n")
    
            print("Alumno registrado exitosamente.")
            time.sleep(2)
            break

        elif(rpta.upper() =="N"):                  
            print("")
            break

        else:
            print("")
            print("Opción no valida, escoja una opción valida")
            print("")

def mostrar_alumnos():

    with open("alumnos.txt", "r") as jsonfile:
        for line in jsonfile:
            alumno_dict = json.loads(line)
            alumno = Alumno(**alumno_dict)
            notas = alumno_dict.get("notas", [])

            if notas:
                max_nota = max(notas)
                min_nota = min(notas)
                prom_nota = sum(notas)/len(notas)
            else:
                max_nota = "No hay notas"
                min_nota = "No hay notas"
                prom_nota = "No hay notas"

            print(f"Alumno: {alumno.nombre}, Máxima nota: {max_nota}, Mínima nota: {min_nota}, Promedio: {prom_nota}")

    Fin_Inf_Alumn = True

    while Fin_Inf_Alumn:
        print("")
        print("Desea ir al menu o salir del programa? (M/0)")
        exit_rpta = input("Respuesta: ")
        if(exit_rpta.upper() =="M"):
            Fin_Inf_Alumn = False
            Fin_Programa = True
            break

        elif(exit_rpta.upper() =="0"):
            Fin_Inf_Alumn = False
            Fin_Programa = False
            break
        else:
            print("")
            print("Opción no valida, escoja una opción valida")
            print("")

    return Fin_Programa

def eliminar_alumnos():

    dni = input("Ingrese el DNI del alumno a eliminar: ")
    nombre_eliminado = ""
    dni_eliminado = ""

    with open("alumnos.txt", "r") as jsonfile:
        for line in jsonfile:
            alumno = json.loads(line)
            if alumno["dni"] == dni:
                nombre_eliminado = alumno["nombre"]
                dni_eliminado = alumno["dni"]

    with open("alumnos.txt", "r") as jsonfile:
        alumnos = [json.loads(line) for line in jsonfile if json.loads(line)["dni"] != dni]

    if nombre_eliminado != "" and dni_eliminado != "" :

        o = True

        while o:
            print(f"Esta seguro que desea eliminar el alumno {nombre_eliminado} de los registros? (Y/N)")
            rpta = input("Respuesta: ")
            if(rpta.upper() =="Y"):
                with open("alumnos.txt", "w") as jsonfile:
                    for alumno in alumnos:
                        json.dump(alumno, jsonfile)
                        jsonfile.write("\n")

                    print("")
                    print(f"Se elimino el registro del alumno {nombre_eliminado} con DNI {dni_eliminado}.")
                    time.sleep(2)
                break

            elif(rpta.upper() =="N"):  
                print("Se cancelo la anulacion de registros.")
                print("")
                time.sleep(2)
                break

            else:
                print("")
                print("Opción no valida, escoja una opción valida")
                print("")
    else:
        print(f"No se encontró ningun registro con el DNI {dni}.")
        time.sleep(2)


def registrar_notas():
    dni = input("Ingrese el DNI del alumno: ")
    notas = []

    with open("alumnos.txt", "r") as jsonfile:
        alumnos = [Alumno(**json.loads(line)) for line in jsonfile if json.loads(line)["dni"] == dni]

    if len(alumnos) == 0:
        print(f"No se encontró ningún registro con el DNI {dni}.")
        time.sleep(2)
        return

    alumno = alumnos[0]

    while len(notas) < 4:
        nota_str = input(f"Ingrese la nota {len(notas)+1}: ")
        nota = int(nota_str)
        notas.append(nota)

    for nota in notas:
        alumno.agregar_nota(nota)

    with open("alumnos.txt", "r+") as jsonfile:
        registros = [json.loads(line) for line in jsonfile]
        jsonfile.seek(0)
        for registro in registros:
            if registro["dni"] == dni:
                registro["notas"] = notas
            json.dump(registro, jsonfile)
            jsonfile.write("\n")

    print(f"Se registraron las notas del alumno {alumno.nombre} con DNI {alumno.dni}.")

    time.sleep(2)


class Docente(Persona):
    def __init__(self, nombre, dni, edad, especialidad):
        super().__init__(nombre, dni, edad)
        self.especialidad = especialidad

    def reporte(self):
        reporte = f"Docente: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"
        return reporte



def registrar_docentes():
    nombre = input("Ingrese el nombre del docente: ")
    dni = input("Ingrese el DNI del docente: ")
    edad = input("Ingrese la edad del docente: ")
    especialidad = input("Ingrese la especialidad del docente: ")

    docente = Docente(nombre, dni, edad, especialidad)

    o = True

    while o:
        print(f"Esta seguro que desea agregar al docente {nombre} a lista de docentes? (Y/N)")
        rpta = input("Respuesta: ")
        if(rpta.upper() =="Y"):
            with open("docentes.txt", "a") as jsonfile:
                json.dump(docente.__dict__, jsonfile)
                jsonfile.write("\n")
    
            print("Docente registrado exitosamente.")
            time.sleep(2)
            break

        elif(rpta.upper() =="N"):                  
            print("")
            break

        else:
            print("")
            print("Opción no valida, escoja una opción valida")
            print("")

def mostrar_docentes():
    with open("docentes.txt", "r") as jsonfile:
        for line in jsonfile:
            docente_dict = json.loads(line)
            docente = Docente(**docente_dict)
            print(f"Nombre: {docente.nombre}, DNI: {docente.dni}, Edad: {docente.edad}, Especializacion: {docente.especialidad}")

        Fin_Inf_Docent = True

        while Fin_Inf_Docent:
            print("")
            print("Desea ir al menu o salir del programa? (M/0)")
            exit_rpta = input("Respuesta: ")
            if(exit_rpta.upper() =="M"):
                Fin_Inf_Docent = False
                Fin_Programa = True
                break

            elif(exit_rpta.upper() =="0"):
                Fin_Inf_Docent = False
                Fin_Programa = False
                break
            else:
                print("")
                print("Opción no valida, escoja una opción valida")
                print("")

    return Fin_Programa

def eliminar_docentes():

    dni = input("Ingrese el DNI del alumno a eliminar: ")
    nombre_eliminado = ""
    dni_eliminado = ""

    with open("docentes.txt", "r") as jsonfile:
        for line in jsonfile:
            docente = json.loads(line)
            if docente["dni"] == dni:
                nombre_eliminado = docente["nombre"]
                dni_eliminado = docente["dni"]

    with open("docentes.txt", "r") as jsonfile:
        docentes = [json.loads(line) for line in jsonfile if json.loads(line)["dni"] != dni]

    if nombre_eliminado != "" and dni_eliminado != "" :
        o = True

        while o:
            print(f"Esta seguro que desea eliminar el docente {nombre_eliminado} de los registros? (Y/N)")
            rpta = input("Respuesta: ")
            if(rpta.upper() =="Y"):
                with open("docentes.txt", "w") as jsonfile:
                    for docente in docentes:
                        json.dump(docente, jsonfile)
                        jsonfile.write("\n")

                    print("")
                    print(f"Se elimino el registro del docente {nombre_eliminado} con DNI {dni_eliminado}.")
                    time.sleep(2)
                break

            elif(rpta.upper() =="N"):  
                print("Se cancelo la anulacion de registros.")
                print("")
                time.sleep(2)
                break

            else:
                print("")
                print("Opción no valida, escoja una opción valida")
                print("")
    else:
        print(f"No se encontró ningun registro con el DNI {dni}.")
        time.sleep(2)


class Menu:
    def __init__(self, nombreMenu, listaOpciones):
        self.nombreMenu = nombreMenu
        self.listaOpciones = listaOpciones

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("\n")
            print("::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                  self.nombreMenu.upper()+"::::::::::::::::::::")          
            print("\n")

            for (key, value) in self.listaOpciones.items():
                print(key+" → "+value)

            print("\n")
            ans = input("Por favor, ingrese su opción: ")
            print("\n")

            if(ans.upper() == "0"):
                print("Hasta, pronto")
                break

            b = 0

            for (key, value) in self.listaOpciones.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False
            else:
                print("Opción no valida, escoja una opción valida")
                time.sleep(1)

        return ans             


    def limpiarPantalla(self):
        def clear():
            return os.system('cls')
           #return os.system('clear')
        clear()   
        
        # os.system('cls')

Arch_Docentes = "docentes.txt"
Arch_Alumnos = "alumnos.txt"

if not os.path.isfile(Arch_Docentes):
    with open(Arch_Docentes, "w") as file:
        pass
if not os.path.isfile(Arch_Alumnos):
    with open(Arch_Alumnos, "w") as file:
        pass    

Home_op = {"Docentes":"1","Alumnos":"2","Exit":"0"}
Main_menu = Menu("Inicio",Home_op)

Docente_op = {"Agregar Docente":"1","Lista de Docentes":"2","Remover Docente":"3","Exit":"0"}
Menu_Docente = Menu("Docentes",Docente_op)

Alumno_op = {"Agregar Alumnos":"1","Lista de Alumnos":"2","Remover Alumnos":"3","Añadir Notas a los Alumnos":"4","Exit":"0"}
Menu_Alumno = Menu("Alumnos",Alumno_op)


f = True
while f:
    ans = Main_menu.show()
    #print(ans)
    if(ans.upper() == "1"):
        Consulta_Menu_Docente = Menu_Docente.show()
        if(Consulta_Menu_Docente.upper() == "1"):
            print("Selecciono la opcion para registrar docentes.")
            print("")
            registrar_docentes()
            print("")

        elif(Consulta_Menu_Docente.upper() =="2"):
            print("Esta es la lista de docentes: ")
            print("")
            f = mostrar_docentes()

        elif(Consulta_Menu_Docente.upper() =="3"):
            print("")
            eliminar_docentes()
            
    elif(ans == "2"):
        Consulta_Menu_Alumno = Menu_Alumno.show()
        if(Consulta_Menu_Alumno.upper() == "1"):
            print("Selecciono la opcion para registrar alumnos.")
            print("")
            registrar_alumnos()
            print("")
        
        elif(Consulta_Menu_Alumno.upper() =="2"):
            print("Esta es la lista de alumnos: ")
            print("")
            f = mostrar_alumnos()

        elif(Consulta_Menu_Alumno.upper() =="3"):
            print("")
            eliminar_alumnos()

        elif(Consulta_Menu_Alumno.upper() =="4"):
            print("")
            registrar_notas()

    elif(ans == "0"):
        f = False


