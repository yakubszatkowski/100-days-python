from django.shortcuts import render
from django.conf import settings
from PIL import Image
from .image_convert import *
import os

from django.http import JsonResponse

# Create your views here.
def home(request):
    
    return render(request, 'index.html', {})


def create(request):

    path_static_img = os.path.join(settings.BASE_DIR, 'app_stickmanshop', 'static', 'img')
    base_img_stickman = Image.open(f'{path_static_img}/base_stickman.png')

    if request.method == "POST":
        request_getdata = request.POST.get('finalItem', None)
        item, color = request_getdata.split('_')
        item_img = Image.open(f'{path_static_img}/{item}.png')
        base_img_stickman.paste(item_img, (0,0), item_img)
        stickman_image_base64 = png_to_base64(base_img_stickman)
        return JsonResponse({'stickman_image': stickman_image_base64})

    else:
        stickman_image_base64 = png_to_base64(base_img_stickman)
        return render(request, 'create.html', {'stickman_image': stickman_image_base64})


def collection(request):

    return render(request, 'collection.html', {})


def profile(request):

    return render(request, 'profile.html', {})
