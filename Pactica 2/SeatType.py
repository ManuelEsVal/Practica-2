from Destination import *

"""
Bueno en principio falta docstring

"""
class SeatType:
    def __init__(self, seat_class:str, porcent:float):
        self.__seat_class = seat_class
        self.__porcent = porcent
        
    def get_class(self):
        return self.__seat_class    
    
    def get_porcent(self):
        return self.__porcent

    """
    Pero para qué le pasamos el porcentaje si ya es un atributo de la clase (que de hecho
    está construida mayormente por eso)?
    """
    def seat_cost(self, destination_cost, porcent:float):    
        self.__destination_cost__ = destination_cost
        self.__porcent__ = porcent
        """
        Cuando usamos self significa que es una varible de la clase, es decir, un atributo.
        No es que no funcion, pero ticket_cost sólo es una variable que existe en el método
        entonces no necesita el self. 
        """
        self.__ticket_cost = (self.__destination_cost__ * ( 1 + self.__porcent__))
        # print(self.__ticket_cost)
        return self.__ticket_cost
