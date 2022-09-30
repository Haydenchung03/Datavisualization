from django.urls import path
from . import views

urlpatterns = [
    # Adding path to url 
    # allow user to search for position in sql database
    path('NetIncome/<int:id>', views.main, name = "main"),
    path('v1/', views.v1, name = "views 1"),
    path('customer/<int:id>', views.customer, name = "Customer Aquisition")
    
]