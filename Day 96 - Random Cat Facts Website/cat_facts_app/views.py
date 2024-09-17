from django.shortcuts import render
from django.http import JsonResponse, response
from .cat_api import *
from .cat_fav_querry import *
from .models import Favorite


# Create your views here.
def home(response):

    return render(response, "index.html", {})


def start(response):

    return render(response, "start.html", {})


def random_cat_picture(response):
    if response.method == "POST":
        cat_favorite_ajax_post_request(response)
    random_cat_data = get_random_cat_picture()
    cat_id = random_cat_data['id']
    cat_favorite = is_cat_favorite(response, cat_id)

    return render(response, "random_cat_picture.html", {'data': random_cat_data, 'id': cat_id, 'favorite': cat_favorite})


def random_cat_picture_by_breed(response):
    if response.method == 'POST':
        cat_favorite_ajax_post_request(response)
        breed_cat_id = response.POST.get('hidden-input')
        breed_name = response.POST.get('search-breed')
        breed_cat_data = get_random_cat_picture_by_breed(breed_cat_id)[0]
        cat_id = breed_cat_data['id']
        cat_favorite = is_cat_favorite(response, cat_id)

        return render(response, "random_cat_picture_by_breed.html", {'data': breed_cat_data,'input': breed_name, 'id': cat_id, 'favorite': cat_favorite})
    
    return render(response, "random_cat_picture_by_breed.html", {'data': {}})


def cat_by_id(response, id):
    if response.method == "POST":
        cat_favorite_ajax_post_request(response)
    data = show_cat_by_id(id)
    cat_favorite = is_cat_favorite(response, id)

    return render(response, "cat.html", {'data': data, 'id': id, 'favorite': cat_favorite})


def browse_cats(response):
    favorite_cats = browse_random_cats()
    
    return render(response, 'browse_cats.html', {'title': 'Browse Cats', 'data': favorite_cats}) 


def browse_favorite_cats(response):
    user_favorite_cats_ids = cat_favorite_user_request(response)
    print(user_favorite_cats_ids)
    favorite_cats = favorite_cat_convert_ids_to_data(user_favorite_cats_ids)

    return render(response, 'browse_cats.html', {'title': 'Favorite Cats', 'data': favorite_cats}) 


def user_profile(response, username):
    user = response.user
    if username == user.username:
        return render(response, 'user_profile.html', {'user': user})
