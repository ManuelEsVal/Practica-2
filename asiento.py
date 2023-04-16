
from funciones import *

class Asiento:
    def __init__(self, tipo, num):
        self.__tipo = tipo
        self.__num = num
        self.__reservaciones = reservaciones(10)

    
