from django.shortcuts import render
from .cat_api import *

# Create your views here.
def home(response):
    return render(response, "index.html", {})


def start(response):
    return render(response, "start.html", {})


def random_cat_picture(response):
    random_cat_data = get_random_cat_picture()
    print(random_cat_data)
    return render(response, "random_cat_picture.html", {'data': random_cat_data})


def random_cat_picture_by_breed(response):
    if response.method == 'POST':
        breed_cat_id = response.POST.get('hidden-input')
        breed_name = response.POST.get('search-breed')
        breed_cat_data = get_random_cat_picture_by_breed(breed_cat_id)
        return render(response, "random_cat_picture_by_breed.html", {'data': breed_cat_data,'input': breed_name})
    
    return render(response, "random_cat_picture_by_breed.html", {'data': {}})

def post_your_cat(response):

    return render(response, 'post_your_cat.html', {'data': {}})
