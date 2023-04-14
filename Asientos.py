import funciones as fun
from random import * 
from tipoAsiento import TipoAsiento 

class Asiento:

    def __init__(self, tipo = TipoAsiento(), numAsiento = "T01"):
        
        self.__tipoAsiento = tipo
        self.__numAsiento = numAsiento
        self.__reservaciones = fun.reservaciones()

    def get_status(self,date):
        
        indice = fun.encontrar(self.__fecha,date)
        status = self.__reservaciones[indice]
        return status
        
    def set_status(self,date):
       
        indice = fun.encontrar(self.__fecha,date)
        status = self.__reservaciones[indice]
        self.__reservaciones[indice] = not status

    def get_numAsiento(self):
        
        return self.__numAsiento

    def get_tipo(self):
        
        return self.__tipoAsiento

    def __str__(self):
       
        return f"Asiento {self.get_numAsiento()}" + "\n" + \
               "Tipo: " + self.get_tipo().get_nombre() + "\n" +\
               
