from django.urls import path
from . import views

urlpatterns = [
    # Adding path to url 
    # allow user to search for position in sql database
    path('NetIncome/<int:id>', views.netIncome, name = "netIncome"),
    path('customer/<int:id>', views.customer, name = "Customer Aquisition"),
    path('', views.home, name = "home")
]