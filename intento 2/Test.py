from Booking import *
from Destination import *
from Seats import *
from SeatType import *


asiento_vip = SeatType('VIP', 0.50)
asiento_trad = SeatType('Tradicional', 0.10)
destinos = [ Destination('Texas', 10000), Destination('Dubai', 20000), Destination('Cancun', 7000)]

#--------------------------#---------------------------#-------------------------------#
#--------------------------#---------------------------#-------------------------------#

def give_D1costs():
    costo_trad_d1 = asiento_trad.seat_cost(destinos[0].get_destination_cost(), asiento_trad.get_porcent())
    costo_vip_d1 = asiento_vip.seat_cost(destinos[0].get_destination_cost(), asiento_vip.get_porcent())
    
    print(destinos[0].get_destination())
    print(asiento_trad.get_class(),':',costo_trad_d1)
    print(asiento_vip.get_class(),':',costo_vip_d1)
    
def give_D2costs():
    costo_trad_d2 = asiento_trad.seat_cost(destinos[1].get_destination_cost(), asiento_trad.get_porcent())
    costo_vip_d2 = asiento_vip.seat_cost(destinos[1].get_destination_cost(), asiento_vip.get_porcent())
    
    print(destinos[1].get_destination())
    print(asiento_trad.get_class(),':',costo_trad_d2)
    print(asiento_vip.get_class(),':',costo_vip_d2)

def give_D3costs():
    costo_trad_d3 = asiento_trad.seat_cost(destinos[2].get_destination_cost(), asiento_trad.get_porcent())
    costo_vip_d3 = asiento_vip.seat_cost(destinos[2].get_destination_cost(), asiento_vip.get_porcent())
    
    print(destinos[2].get_destination())
    print(asiento_trad.get_class(),':',costo_trad_d3)
    print(asiento_vip.get_class(),':',costo_vip_d3)

""" give_D1costs()
give_D2costs()
give_D3costs()
 """
#--------------------------#---------------------------#-------------------------------#
#--------------------------#---------------------------#-------------------------------#

reservaciones = Booking(10)
reservaciones.reservations()

asientos = Seats(50)
asientos_tipos = [asiento_trad.get_class(), asiento_vip.get_class()]
lista_asientos = asientos.seat_distribution( asientos_tipos,'T', 'V', 30)

