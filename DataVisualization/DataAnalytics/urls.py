from django.urls import path
from . import views

urlpatterns = [
    # Adding path to url 
    # allow user to search for position in sql database
    path('calculations/<int:id>', views.Calculations, name = "calculations"),
    path('', views.home, name = "home"),
    path('login/', views.login, name = "login"),
    path('contact/', views.contact, name = "contact")
]