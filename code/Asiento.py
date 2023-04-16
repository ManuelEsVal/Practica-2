
from functions import *

class Seat:
    def __init__(self, type, num):
        self.__type = type
        self.__num = num
        self.__reservations = reservations(10)

    def get_tipo(self):
        """
        Params:
            None
        Return:
            tipo(Objet): Objeto de la clase TipoAsiento
        """
        return self.__tipo