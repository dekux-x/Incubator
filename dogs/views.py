from django.shortcuts import render
import requests
from django.http import JsonResponse, HttpResponse, Http404
from django.core.exceptions import BadRequest

# Create your views here.
def index(request):
    if request.method == "GET":
        page = int(request.GET.get('page')) if request.GET.get('page') != None else 1
        offset = 10
        start = (page - 1) * offset
        end = page * offset
        catalog = []
        dogs = list(get_dogs())
        if start > len(dogs) or start < 0:
            raise BadRequest("Page doesn't exist")
        for i in dogs[start:end]:
            image = get_random(i)
            catalog.append([i,image])
        previous = None if page==1 else page -1
        next_p = None if page * offset >= len(dogs) else page + 1
        return render(request, "dogs/index.html", {"catalog": catalog,"dogs": dogs ,"previous": previous, "next": next_p})
    else:
        raise BadRequest("Bad method")
    

def detail(request, breed):
    if request.method == "GET":
        images = get_dog(breed)
        if images == "Breed not found (master breed does not exist)":
            raise Http404(	"Breed not found (master breed does not exist)")
        dogs = get_dogs()
        return render(request, "dogs/detail.html", {"breed": breed , "images": images, "dogs": dogs})
    else:
        raise BadRequest("Bad method")
    

def get_dogs():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    data = response.json()
    return data["message"]

def get_random(breed):
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    data = response.json()
    return data["message"]

def get_dog(breed):
    url = f'https://dog.ceo/api/breed/{breed}/images/'
    response = requests.get(url)
    data = response.json()
    return data["message"]