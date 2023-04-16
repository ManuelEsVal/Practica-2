from seat_type import TipoAsiento
from reservations import Reservation

class Seat:
    def __init__(self, tipo, num):
        self.__tipo = tipo
        self.__num = num
        self.__reservations = Reservation(10)
        
    def get_tipo(self):
        return self.__tipo
        
    def seat_distribution(self):
        tipoAsiento = [TipoAsiento('Tradicional', 0.10), TipoAsiento("VIP",0.50)]
        
        asientos = []
        j = 0
        for i in range(50):

            if i <= 30:
                aux = "T"
                tipo = tipoAsiento[0]
            else:
                aux = "V"
                tipo = tipoAsiento[1]

            j += 1
            if j >= 10 and j <= 30:
                num = aux + str(j)
            elif j > 30:
                j = 0
                continue
            else:
                num = aux + "0"+ str(j)

            asientos.append(Seat(tipo,num))
        pass