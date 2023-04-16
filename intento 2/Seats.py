from Destination import *
from SeatType import *

class Seats:
    def __init__(self, seats_number) -> None:
        self.__seats_number = seats_number
    
    def seat_cost(self):
        self.ticket_cost = (self.get_destination_cost() * ( 1 +  self.get_porcent() ))
        return self.ticket_cost
    
    def seat_distribution(self, , ):