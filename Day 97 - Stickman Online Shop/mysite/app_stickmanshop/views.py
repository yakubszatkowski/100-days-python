from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from PIL import Image
from .image_convert import *
from .models import SavedStickman
import os, json


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
        name = request.POST.get('stickman_name', None)

        if save:
            last_item_data = request.session.get('last_item_data', None)
            last_image_data = request.session.get('last_image_data', None)
            if last_item_data:
                stickman = SavedStickman(
                    stickman_name=name, 
                    stickman_clothes=last_item_data,
                    stickman_img_base64=last_image_data
                )
                stickman.save()
                print(len(name))
                request.user.saved_stickmen.add(stickman)
                request.session['last_item_data'], request.session['last_image_data'] = None, None

        elif purchase:
            print('purchased')

        elif ajax_data:
            if item_data:
                dressed_stickman = dressing_stickman(path_static_img, base_img_stickman, item_data)
                context['stickman_image'] = png_to_base64(dressed_stickman)
                context['money_total'] = stickman_pricing(item_data)
                request.session['last_item_data'] = item_data
                request.session['last_image_data'] = context['stickman_image']
            else:
                context['stickman_image'] = png_to_base64(base_img_stickman)
                context['money_total'] = '0.00'
            return JsonResponse(context)

    return render(request, 'create.html', context)


def collection(request):
    user_saved_stickmans = SavedStickman.objects.filter(user=request.user)

    ids = [stickman.id for stickman in user_saved_stickmans]
    print(ids)

    return render(request, 'collection.html', {'stickmans_data': user_saved_stickmans})


def profile(request):

    return render(request, 'profile.html', {})
