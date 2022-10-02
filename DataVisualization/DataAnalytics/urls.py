from django.urls import path
from . import views

urlpatterns = [
    # Adding path to url 
    # allow user to search for position in sql database
    path('Calculations/<int:id>', views.Calculations, name = "Calculations"),
    path('', views.home, name = "home")
]