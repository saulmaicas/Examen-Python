from autor import Autor
from libro import Libro


def get_list(nombre):
    with open(nombre, 'r', encoding='utf-8') as f:
        solucion = {}
        lineas = f.readlines()
        lineas = [a.strip() for a in lineas]
        for frase in lineas:
            palabras = frase.split(' ')
            for palabra in palabras:
                print(palabra)
                if len(palabra) in solucion:
                    if palabra not in solucion[len(palabra)]:
                        solucion[len(palabra)].append(palabra)
                else:
                    solucion[len(palabra)] = []
                    solucion[len(palabra)].append(palabra)
        return solucion
       

get_list('palabras.txt')


def mas_antiguos (lista, anyo):
    lista_titulos = []
    print (lista)



#----------------main-----------------------------------


l1 = Libro (titulo="Golondrinas" , anyo=2010 , autor = Autor("1", "Francisco", "Primero"))
#l2 =  Libro("Francisco", "La teoria de la rela" , 2021)
#l3 =  Libro("Francisco", "La teoria de la rela" , 2021)
lista = []
lista.append(l1)
#lista.append(l2)
#lista.append(l3)
print (lista)

#llamada_antiguos = mas_antiguos(lista, 2010)