import os
import time
from controller import Controller

controller = Controller()
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


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
                print("Chau chau")
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
               #return os.system('cls')
           return os.system('clear')
        clear()   
        
        # os.system('cls')

class View:
    
    def mostrarMenu(self):
        opcionesLibros = {"Create":"1","Get":"2","Update":"3","Delete":"4","Exit":"0"}
        MenuLibros = Menu("Libros",opcionesLibros)

        f = True
        while f:
            ans = MenuLibros.show()
            if(ans == "0"):
                f = False
            if(ans == "1"):              
                titulo = input("Escribe el nombre del Libro: ")
                fecPublicacion = input("Escribe la Fecha de Publicacion: ")
                isbn = input("Escribe el ISBN: ")
                autor = int(input("Escribe el codigo de AUTOR: "))
                if(controller.crearLibro(titulo,fecPublicacion,isbn,autor)):
                    print("El libro se creo correctamente")
                    input("Continuar")
