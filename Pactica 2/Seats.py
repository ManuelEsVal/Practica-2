from Destination import *
from SeatType import *
from Booking import *

class Seats:
    """
    Pero le falta qué tipo de asinto es, es decir, un objeto SeatType como atributo
    """
    def __init__(self, seats_number:int) -> None:
        self.__seats_number = seats_number

    """
    Lo mismo que en la clase anterior, self sólo se usa para hacer referencia a los atributos y métodos de la clase,
    no para variables que solo existan dentro del método
    """
    def seat(self, _class, num):
        self.__class = _class
        self.__num = num

        
        self.seat_list = [self.__class, self.__num]
        return self.seat_list
    
    def seat_distribution(self, class_list:list, class_letter1:str, class_letter2:str, fist_range:int):
        """
        No es necesario definir atributos con los parámetros, eso solo se hace en el constructor.
        Aquí se trabaja directamente con los parámetros
        """
        self.class_letter1 = class_letter1
        self.class_letter2 = class_letter2
        self.class_list = class_list
        self.first_range = fist_range
        
        seat_class = class_list #[trad, vip]
        print(seat_class)
        
        j = 0
        # print(self.__seats_number)
        seat = []

        """
        Pero los objetos ya tendrían que definirse con su número, no calacularse dentro.
        De hecho la clase seats debería ser seat porque sólo debe modelarse uno
        """
        for i in range(self.__seats_number + 1):

            if i <= self.first_range:
                aux = str(self.class_letter1)
                _type = seat_class[0]
            else:
                aux = str(self.class_letter2)
                _type = seat_class[1]

            j += 1
            
            if j >= 10 and j <= self.first_range:
                num = aux + str(j)
            elif j > self.first_range:
                j = 0
                continue
            else:
                num = aux + "0"+ str(j)
            print(num)
            
            seat.append(self.seat( _type, num))
            
        print(seat)
      
