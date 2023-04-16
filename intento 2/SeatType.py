class SeatType:
    def __init__(self, seat_class, porcent):
        self.__seat_class = seat_class
        self.__porcent = porcent
        
    def get_class(self):
        return self.__seat_class    
    
    def get_porcent(self):
        return self.__porcent