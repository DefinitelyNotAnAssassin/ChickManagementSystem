from Models.models import *
import django_tables2 as tables

class ReservationTable(tables.Table):
    class Meta:
        model = Reservation
        fields = ['name', 'hatch', 'date', 'rhode_island_red', 'barred_plymouth_rock', 'black_australorp', 'amount', 'remarks']
        
        
        