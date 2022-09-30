from django.urls import path
from . import views

urlpatterns = [
    # Adding path to url 
    path('', views.main, name = "main"),
    path('v1/', views.v1, name = "views 1")
]