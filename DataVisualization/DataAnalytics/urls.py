from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Adding path to url 
    # allow user to search for position in sql database
    path('calculations/', views.Calculations, name = "calculations"),
    path('', views.home, name = "home"),
    path('login/', views.login, name = "login"),
    path('contact/', views.contact, name = "contact")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)