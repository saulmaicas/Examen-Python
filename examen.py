from autor import Autor
from libro import Libro



def get_list (nombre):

    f = open("palabras.txt", mode="rt", encoding="utf-8")

    #leemos los restantes
    contenido = []
    contenido = f.readlines()
    print (contenido)

    f.close()

def mas_antiguos (lista, anyo):


#----------------main-----------------------------------

llamada = get_list("palabras.txt")


l1 =  Libro("Francisco", "La teoria de la rela" , 2021)
l2 =  Libro("Francisco", "La teoria de la rela" , 2021)
l3 =  Libro("Francisco", "La teoria de la rela" , 2021)
lista = []
lista.append(l1)
lista.append(l2)
lista.append(l3)

llamada_antiguos = mas_antiguos(lista, 2010)