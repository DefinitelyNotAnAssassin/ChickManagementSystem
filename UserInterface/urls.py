from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('batch_date/<str:date>', views.batch_date, name = "batch date")
]
