from django.shortcuts import render
from django.http import JsonResponse
from .cat_api import *

def favorite_response(response):
    if response.method == "POST":
        checkbox_signal = response.POST.get('checkbox-signal')
        print(checkbox_signal)


# Create your views here.
def home(response):
    return render(response, "index.html", {})


def start(response):
    return render(response, "start.html", {})


def random_cat_picture(response):
    # favorite_response(response)
    random_cat_data = get_random_cat_picture()

    return render(response, "random_cat_picture.html", {'data': random_cat_data})


def random_cat_picture_by_breed(response):
    if response.method == 'POST':
        breed_cat_id = response.POST.get('hidden-input')
        breed_name = response.POST.get('search-breed')
        breed_cat_data = get_random_cat_picture_by_breed(breed_cat_id)[0]
        print(breed_cat_data)

        return render(response, "random_cat_picture_by_breed.html", {'data': breed_cat_data,'input': breed_name})
    
    return render(response, "random_cat_picture_by_breed.html", {'data': {}})


def cat_by_id(response, id):
    data = show_cat_by_id(id)

    return render(response, "cat.html", {'data': data})


def browse_cats(response):
    cats_data = browse_random_cats()
    
    return render(response, 'browse_cats.html', {'data': cats_data})

