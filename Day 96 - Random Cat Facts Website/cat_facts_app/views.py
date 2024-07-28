from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "index.html", {})

def start(response):
    return render(response, "start.html", {})