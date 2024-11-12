from django.shortcuts import render, redirect
from django.conf import settings
from PIL import Image
from .image_convert import *
import os, json

from django.http import JsonResponse

# Create your views here.
def home(request):
    
    return render(request, 'index.html', {})


def create(request):
    path_static_img = os.path.join(settings.BASE_DIR, 'app_stickmanshop', 'static', 'img')
    base_img_stickman = Image.open(f'{path_static_img}/base_stickman.png')
    stickman_image_base64 = png_to_base64(base_img_stickman)
    context = {'stickman_image': stickman_image_base64, 'money_total': '0.00'}

    if request.method == "POST":
        ajax_data = request.POST.get('ajax_data', None)
        item_data = json.loads(ajax_data) if ajax_data else {}
        save = request.POST.get('save_stickman', None)
        purchase = request.POST.get('purchase_stickman', None)

        if save and item_data:
            print('saved')
        elif purchase and item_data:
            print('purchased')
        elif ajax_data:
            if item_data:
                context['money_total'] = pricing(item_data)
                for item in item_data:
                    item_color = item_data[item]
                    item_img = Image.open(f'{path_static_img}/{item}.png')
                    base_img_stickman.paste(item_img, (0,0), item_img)
                    colored_picture = fill_color(base_img_stickman, item, item_color)
                    context['stickman_image'] = png_to_base64(colored_picture)
            else:
                context['stickman_image'] = png_to_base64(base_img_stickman)
                context['money_total'] = '0.00'
            return JsonResponse(context)

    return render(request, 'create.html', context)


def collection(request):

    return render(request, 'collection.html', {})


def profile(request):

    return render(request, 'profile.html', {})
