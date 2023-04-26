from Booking import *
from Destination import *
from functions import *
from Seats import *
from SeatType import *

name = input('Nombre: ')

"""
Y el usuario cómo sabe a donde puede ir si no se le muestran los destinos?
"""
print('\nHola',name,'¿a dondé te gustaría ir?')

t = 0
"""
Recuerden que estamos modelando entidades, no scripts.
lugares es una simple lista, y no queremos trabajar con la lista, sino con un método de una clase
que dentro tenga el código que tinen aquí.
"""
for i in lugares:
    t += 1
    print('\n',str(t) + '-',i,'\n')
    print('fechas disponibles y precio de vuelo: \n')
    for d in lista_fechas:
        print(d)
    
destination_selection = input('\nselección: ')

if destination_selection == lugares[0]:
    pass
elif destination_selection == lugares[1]:
    pass
elif destination_selection == lugares[2]:
    pass
else:
    pass
