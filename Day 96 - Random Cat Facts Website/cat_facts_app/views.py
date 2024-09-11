from django.shortcuts import render
from django.http import JsonResponse
from .cat_api import *
from .cat_fav_querry import *
from .models import FavoriteList
from django.contrib.auth.models import User


# Create your views here.
def home(response):
    return render(response, "index.html", {})


def start(response):
    return render(response, "start.html", {})


def random_cat_picture(response):
    if response.method == "POST":
        cat_favorite_ajax_post_request(response)
    random_cat_data = get_random_cat_picture()

    return render(response, "random_cat_picture.html", {'data': random_cat_data, 'id': random_cat_data['id']})


def random_cat_picture_by_breed(response):
    if response.method == 'POST':
        cat_favorite_ajax_post_request(response)
        breed_cat_id = response.POST.get('hidden-input')
        breed_name = response.POST.get('search-breed')
        breed_cat_data = get_random_cat_picture_by_breed(breed_cat_id)[0]

        return render(response, "random_cat_picture_by_breed.html", {'data': breed_cat_data,'input': breed_name, 'id': breed_cat_data['id']})
    
    return render(response, "random_cat_picture_by_breed.html", {'data': {}})


def cat_by_id(response, id):
    if response.method == "POST":
        cat_favorite_ajax_post_request(response)
    data = show_cat_by_id(id)
    return render(response, "cat.html", {'data': data, 'id': id})


def browse_cats(response):
    cats_data = browse_random_cats()
    
    return render(response, 'browse_cats.html', {'data': cats_data})
