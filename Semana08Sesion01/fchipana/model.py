from db import db

class Libros:
    def __init__(self, titulo, fecPublicacion, isbn, autor) -> None:
        # self.id = id
        self.titulo = titulo
        self.fecPublicacion = fecPublicacion
        self.isbn = isbn
        self.autor = autor

    def crearLibro(self):
        conn = db()
        query = f'''INSERT INTO public."Libros"(titulo,"fePublicacion",isbn,autor)
        values('{self.titulo}','{self.fecPublicacion}','{self.isbn}',{self.autor})'''
        return conn.ejecutarBDD(query)
    
    def traerLibros(self):
        conn = db()
        query = f"select * from Libros"
        return conn.consultarBDD(query)
    
    def traerLibro(self, nombre):
        conn = db()
        query = f"select * from Libros where nombre  = '{self.nombre}'"
        return conn.consultarBDD(query)
    
