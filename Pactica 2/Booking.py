import random
from datetime import datetime, timedelta, date

class Booking:
    def __init__(self, n, obj_list) -> None:
        self.obj_list = obj_list
        self.n = n
        self.dates = []
        self.today = date.today()
        """
        De hechos les pedí 10 fechas aleatorias, para mostrar las 10 por cada destino
        """
        self.tomorrow = self.today + timedelta(days=12)
        
    def available_dates(self):
        for obj in self.obj_list:
            date_list = []
            """
            pero se pueden repetir porque no hay mucha diferencia de días.
            Además si si n vale por ejemplo 50, su lista de 50 fechas va a tener fechas repetidas
            """
            for i in range(self.n):
                start_date = self.today
                end_date = self.tomorrow
                time_between_dates = end_date - start_date
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)
                random_date = start_date + timedelta(days=random_number_of_days)
                date_list.append(random_date)
            self.dates.append(date_list)
        return date_list

    """
    Solo tenemos una lista de booleanos verdaderos
    """
    def reservations(self):
        reservaciones = []
        for i in range(self.n):
            reservaciones.append(True)
        return reservaciones
