from django.shortcuts import render
from django.conf import settings
from PIL import Image
from io import BytesIO
import os, base64

# Create your views here.
def home(request):
    
    return render(request, 'index.html', {})


def create(request):
    if request.method == "POST":
        request_getdata = request.POST.get('finalItem', None)
        print(request_getdata)

    path_static_img = os.path.join(settings.BASE_DIR, 'app_stickmanshop', 'static', 'img')
    base_img_stickman = Image.open(f'{path_static_img}/base_stickman.jpg').convert('RGB')
    
    buffer_stickman = BytesIO()
    base_img_stickman.save(buffer_stickman, 'JPEG')
    buffer_stickman.seek(0)
    stickman_image_base64 = base64.b64encode(buffer_stickman.getvalue()).decode('utf-8')

    return render(request, 'create.html', {'stickman_image': stickman_image_base64})


def collection(request):

    return render(request, 'collection.html', {})


def profile(request):

    return render(request, 'profile.html', {})
