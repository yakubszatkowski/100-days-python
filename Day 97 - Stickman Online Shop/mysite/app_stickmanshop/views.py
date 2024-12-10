from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .image_convert import png_to_base64, dressing_stickman
from .models import SavedStickman
from .utils import save_stickman, stickman_pricing
from PIL import Image
import os, json


def home(request):
    return render(request, 'index.html', {})


def profile(request):
    return render(request, 'profile.html', {})


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
            save_stickman(request, name)
            return redirect('collection')

        elif purchase:
            stickman_id = save_stickman(request, name)
            return redirect(f'payment/stickman/{stickman_id}')

        elif ajax_data:
            if item_data:
                dressed_stickman = dressing_stickman(path_static_img, base_img_stickman, item_data)
                context['stickman_image'] = png_to_base64(dressed_stickman)
                context['money_total'] = stickman_pricing(item_data)
                request.session['last_item_data'] = item_data
                request.session['last_image_data'] = context['stickman_image']
                request.session['last_price'] = context['money_total']
            else:
                context['stickman_image'] = png_to_base64(base_img_stickman)
                context['money_total'] = '0.00'
            return JsonResponse(context)

    return render(request, 'create.html', context)


def collection(request):
    user_saved_stickmans = SavedStickman.objects.filter(user=request.user)

    return render(request, 'collection.html', {'stickmans_data': user_saved_stickmans})
