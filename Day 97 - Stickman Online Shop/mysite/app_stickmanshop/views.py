from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'index.html', {})


def create(request):

    return render(request, 'create.html', {})


def collection(request):

    return render(request, 'collection.html', {})


def profile(request):

    return render(request, 'profile.html', {})
