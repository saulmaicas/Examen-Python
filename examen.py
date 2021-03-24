def get_list (nombre):

    f = open("palabras.txt", mode="rt", encoding="utf-8")

    #leemos los restantes
    contenido = []
    contenido = f.readlines()
    print (contenido)

    diccionario = {}
    contador = 0

    for i in contenido:
        diccionario = contenido [i]
    print (diccionario)


    f.close()

#----------------main-----------------------------------

llamada = get_list("palabras.txt")
