from pprint import pprint as pp

class Cinema:

    def __init__(self,rows,seats_per_row):
        """
        Args:
            rows: filas de la sala
            seats_per_row: butacas de cada fila    
        """
        self.__rows = rows
        self.__seats_per_row = seats_per_row
        self.__seating = []
    
    def create_cinema_seating(self):
        """
        Inicializa el seating de la sala, que es una lista de diccionarios.
          - Cada elemento de la lista representa una fila de butacas, empezando por la fila 0 que esta en la posicion 0.
          - Cada fila tiene un diccionario para representar las butacas de esa fila.
          - Las claves del diccionario son cada una de las butacas de esa fila (1, 2, 3, etc.).
        """        
        row = { i : None for i in range(1, self.__seats_per_row+1) }        
        for j in range(1, self.__rows+1):
            self.__seating.append(row)
        
    def print_seating(self):
        """
        Imprime el seating de la sala
        """
        pp(self.__seating)

    def book_seat(self,row,seat):
        """
        Marca una butaca como ocupada.
        Args:
            row: la fila de la butaca
            seat: el numero de la butaca
        """
        asientos = self.__seating
        for valores in asientos:    
            if self.__seating[row][seat] is None:
                self.__seating[row][seat] = "occupied"

    def count_free_seats(self,rows_seats,total):
        """
        Calcula la cantidad de butacas libres que hay en una lista
        Args:
            rows_seats: lista de butacas a buscar
            total: valor inicial donde se acumularÃ¡ el total
        """
        total = 0 
        plan_asientos = rows_seats
        for valores in plan_asientos:
            if valores != None:
                contador += 1
        return total

#------------------------------------------- MAIN -----------------------------------------------
cinema = Cinema(rows=10, seats_per_row=8)

#ERROR 1: al reservar una butaca (p.e. fila 2 butaca 4) e imprimir el seating, veo que aparece como ocupada la 4 de cada fila, y no solo de la fila 2.
print("------------- Error 1 -----------------")
cinema.create_cinema_seating()
cinema.book_seat(2,4)
cinema.print_seating()

#ERROR 2: le paso la lista de "seats" donde deberÃ­a haber 2 libres y me dice que hay 0.
print("\n------------- Error 2 -----------------")
seats = [(2,4), (3,1), (5,2)]
total = 0
cinema.count_free_seats(seats,total)
print("total: "+str(total))

#ERROR 3: quiero modificar la butaca (2,4) de la lista anterior para que sea la (3,4) y no me deja.
print("\n------------- Error 3 -----------------")
seats[0][1]=3
total = 0
cinema.count_free_seats(seats,total)
print("total: "+str(total))
        