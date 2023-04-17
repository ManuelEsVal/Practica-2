from datetime import * 

class Booking:
    def __init__(self, n):
        self.n = n
    
    def available_dates(self):
        date = []
        _today = date.today()
        for i in range(31):
            dia = timedelta(i) # Un día, dos días etc
            date.append(_today + dia)
        return date
    
    def reservations(self) -> list:
        reservaciones = []
        for i in range(self.n):
            reservaciones.append(True)
        print(reservaciones)
        return reservaciones
