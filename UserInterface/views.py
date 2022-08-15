from django.shortcuts import HttpResponse
from Models.models import *
from django.db.models import Q, Count, Sum
def index(request):
    hatch = HatchingBatch.objects.filter(id = 2).aggregate(Sum('reservation__amount'))
    print(hatch)

    return HttpResponse("Hello, world")