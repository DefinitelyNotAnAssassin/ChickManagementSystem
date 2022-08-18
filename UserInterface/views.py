from django.shortcuts import render
from Models.models import *
from django.db.models import Q, Count, Sum, F
from .tables import ReservationTable
from .filter import ReservationFilter
def index(request):
    current_stock = Stock.objects.annotate(reserved_rir = Sum("hatch_batch__reservation__rhode_island_red"), reserved_ba = Sum("hatch_batch__reservation__black_australorp"), reserved_bpr = Sum("hatch_batch__reservation__barred_plymouth_rock")).get(id = 1)
    current_rir = current_stock.hatch_batch.rhode_island_red - current_stock.reserved_rir
    current_ba = current_stock.hatch_batch.black_australorp - current_stock.reserved_ba
    current_bpr = current_stock.hatch_batch.barred_plymouth_rock - current_stock.reserved_bpr
    print(current_rir, current_ba, current_bpr)
    
    filtr = ReservationFilter(request.GET)
    table = ReservationTable(filtr.qs)
    items = {
        'current_rir' : current_rir,
        'current_ba' : current_ba,
        'current_bpr': current_bpr,
        'table': table,
        'filter': filtr

    }



    return render(request, "UserInterface/index.html", context=items)
def batch_date(request, date):
    return render(request, 'UserInterface/hatch_batch.html')