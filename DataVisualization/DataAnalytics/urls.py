from django.urls import path
from .views import main

urlpatterns = [
    # Adding path to url 
    path('', main)
]