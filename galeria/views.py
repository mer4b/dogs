from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
#def hello(request):
 #   return HttpResponse("hola Django")

def getAlbums(request):
    URL_API= "https://jsonplaceholder.typicode.com/albums"

    respose = request.get(URL_API)

    if respose.status_code == 200:
        productos = respose.json()
    else:
        return "Pagina no encontrada",404

    
    #return HttpResponse(respose) or []
    return render(request,'album.html',{'album': respose})

def obtener_breeds(request):
    URL_BREEDS = "https://dog.ceo/dog-api/breeds-list"

    try:
        response= requests.get(URL_BREEDS)

        if response.status_code == 200:
            breed = response.json()['message']
        else:
            print(f"error en la solicitud: {response.status_code} ")
            breed=[]
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e} ")
        breed=[]
        
    print(breed)
    
    return render(request,'index.html',{'breed': breed})
    

                