from Booking import *
from Destination import *
from Seats import *
from SeatType import *

asientos = Seats(50)

asiento_vip = SeatType('VIP', 0.10)
asiento_trad = SeatType('Tradicional', 0.10)

asientos_tipos = [asiento_trad.get_class(), asiento_vip.get_class()]

destinos = [ Destination( 'Texas', 10000)\
           , Destination( 'Dubai', 20000)\
           , Destination( 'Cancun', 7000)]

reservaciones = Booking(10)

reservaciones.reservations()

distribucion = asientos.seat_distribution( asientos_tipos,'T', 'V', 30)