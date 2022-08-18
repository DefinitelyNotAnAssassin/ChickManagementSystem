import django_filters as filter

from Models.models import * 

class ReservationFilter(filter.FilterSet):

    class Meta:
        model = Reservation
        fields = ['name', 'date', 'hatch__hatch_date']