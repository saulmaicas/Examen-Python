from autor import Autor

class Libro:
     
    def __init__(self, titulo, anyo, autor):
        self.__titulo = titulo
        self.__anyo = anyo
        self.__autor = autor
        self.__seating = Autor.get_id()

    def get_titulo (self):
        return self.__titulo

    def get_anyo (self):
        return self.__anyo

#-----------main-----------------

l1 = Libro(titulo="Las golondrinas" , anyo= 2010 ,  autor = Autor("1", "Francisco", "Primero"))
print (l1)