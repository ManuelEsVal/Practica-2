import random
from datetime import datetime, timedelta

class Booking:
    def __init__(self, n, obj_list) -> None:
        self.obj_list = obj_list
        self.n = n
        self.dates = []
    
    def available_dates(self):
        for obj in self.obj_list:
            date_list = []
            for i in range(10):
                start_date = datetime(2022, 1, 1)
                end_date = datetime(2023, 12, 31)
                time_between_dates = end_date - start_date
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)
                random_date = start_date + timedelta(days=random_number_of_days)
                date_list.append(random_date)
            self.dates.append(date_list)
        return date_list
    
    def reservations(self):
        reservaciones = []
        for i in range(self.n):
            reservaciones.append(True)
        return reservaciones
