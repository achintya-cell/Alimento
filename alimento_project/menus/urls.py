from django.urls import path,include
from . import views

urlpatterns = [
    path('items/',views.items,name="items"),
    path('orders/',views.orders,name="orders"),
]