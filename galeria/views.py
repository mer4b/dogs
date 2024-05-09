from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
#def hello(request):
 #   return HttpResponse("hola Django")

def getAPI(request):
    URL_API= "https://jsonplaceholder.typicode.com/albums"

    respose = request.get(URL_API)

    if respose.status_code == 200:
        productos = respose.json()

    
        return HttpResponse(respose) or []

def obtener_breeds(request):
    URL_BREEDS = "https://dog.ceo/api/breeds/list/all"

    try:
        response= requests.get(URL_BREEDS)

        if response.status_code == 200:
            breed = response.json()
        else:
            print(f"error en la solicitud: {response.status_code} ")
            breed=[]
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e} ")
        breed=[]
    
    return render(request,'index.html',{'breed': breed})

                
