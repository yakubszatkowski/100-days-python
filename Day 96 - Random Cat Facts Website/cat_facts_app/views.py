from django.shortcuts import render
from .cat_api import *

# Create your views here.
def home(response):
    return render(response, "index.html", {})


def start(response):
    return render(response, "start.html", {})


def random_cat_picture(response):
    random_cat_data = get_random_cat_picture()[0]
    print(random_cat_data)
    return render(response, "random_cat_picture.html", {'data': random_cat_data})


def random_cat_picture_by_breed(response):
    if response.method == 'POST':
        search_breed = response.POST.get('search-breed')
        print(search_breed)
        

    return render(response, "random_cat_picture_by_breed.html", {})

