from Destination import *


class SeatType:
    def __init__(self, seat_class:str, porcent:float):
        self.__seat_class = seat_class
        self.__porcent = porcent
        
    def get_class(self):
        return self.__seat_class    
    
    def get_porcent(self):
        return self.__porcent
    
    def seat_cost(self, destination_cost, porcent:float):    
        self.__destination_cost__ = destination_cost
        self.__porcent__ = porcent
          
        self.__ticket_cost = (self.__destination_cost__ * ( 1 + self.__porcent__))
        # print(self.__ticket_cost)
        return self.__ticket_cost