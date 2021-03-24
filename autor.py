class Autor:
     
    def __init__(self, id, nombre, apellido):
        self.__id_autor = id
        self.__nombre = nombre
        self.__apellido = apellido

    def get_id (self):
        return self.__id_autor

    def get_nombre (self):
        return self.__nombre

    def get_apellido (self):
        return self.__apellido

#---------------main----------------------

a1 = ("1", "Francisco", "Primero")
#print (a1)