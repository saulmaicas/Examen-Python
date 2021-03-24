from libro import Libro
from autor import Autor
from  examen import *

l1 = Libro ("Golondrinas" , 2010 , autor = Autor("1", "Francisco", "Primero"))
#l2 =  Libro("Francisco", "La teoria de la rela" , 2021)
#l3 =  Libro("Francisco", "La teoria de la rela" , 2021)
lista = []
lista.append(l1)
#lista.append(l2)
#lista.append(l3)
print (lista)

#llamada_antiguos = mas_antiguos(lista, 2010)