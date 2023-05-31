from model import Libros

class Controller:
    def crearLibro(self,titulo, fePublicacion,isbn,autor):
        libro = Libros(titulo, fePublicacion,isbn,autor)
        return libro.crearLibro()
    
    def traerLibros(self):
        libros = Libros()
        return libros.traerLibros()
    
    def traerLibro(self,titulo):
        libro = Libros(titulo=titulo)
        return libro.traerLibro()