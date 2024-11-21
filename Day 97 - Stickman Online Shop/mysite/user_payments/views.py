from django.shortcuts import render, HttpResponse

# Create your views here.
def product_page(request):
    return HttpResponse('<h1>product_view</h1>')


def payment_successful(request):
    return HttpResponse('<h1>payment_successful</h1>')


def payment_cancelled(request):
    return HttpResponse('<h1>payment_cancelled</h1>')

