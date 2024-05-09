from django.urls import path
from galeria.views import obtener_breeds,getAlbums

urlpatterns = [
    path('',obtener_breeds),
     path('album/',getAlbums),
]