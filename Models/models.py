from turtle import ondrag
from django.db import models


class HatchingBatch(models.Model):
    hatch_date = models.DateField()
    incubator = models.CharField(max_length=32)
    rhode_island_red = models.IntegerField(default=0)
    barred_plymouth_rock = models.IntegerField(default=0)
    black_australorp = models.IntegerField(default=0)
    

    

class Reservations(models.Model):
    date = models.DateField()
    hatch = models.ForeignKey(HatchingBatch, related_name="reservation", on_delete=models.CASCADE)
    is_done = models.BooleanField()
    is_delivery = models.BooleanField()
    shipping_fee = models.IntegerField()
    amount = models.IntegerField() 

#The design of this particular model is not yet finalized
class Stocks(models.Model):
    hatch = models.OneToOneField(HatchingBatch, on_delete=models.CASCADE, related_name="stock")
    


    

    

# Create your models here.
