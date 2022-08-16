from turtle import ondrag
from django.db import models


class HatchingBatch(models.Model):
    hatch_date = models.DateField()
    incubator = models.CharField(max_length=32)
    rhode_island_red = models.IntegerField(default=0)
    barred_plymouth_rock = models.IntegerField(default=0)
    black_australorp = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.hatch_date}"
class Reservation(models.Model):
    name = models.CharField(max_length=32)
    date = models.DateField()
    hatch = models.ForeignKey(HatchingBatch, related_name="reservation", on_delete=models.CASCADE)
    is_done = models.BooleanField()
    is_delivery = models.BooleanField()
    shipping_fee = models.IntegerField()
    rhode_island_red = models.IntegerField(default=0)
    barred_plymouth_rock = models.IntegerField(default=0)
    black_australorp = models.IntegerField(default=0)
    amount = models.IntegerField() 
    remarks = models.CharField(max_length=255, default="")
    def __str__(self):
        return f"{self.name} | {self.date}"

class Stock(models.Model):
    hatch_batch = models.ForeignKey(HatchingBatch, on_delete=models.CASCADE)
    

    

# Create your models here.
