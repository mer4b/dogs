from django.urls import path

from .views import getAPI, obtener_breeds

urlpatterns = [
    path('', obtener_breeds, name='obtener_breeds'),
    path('api/',getAPI, name='getAPI'),
]