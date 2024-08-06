from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('random_cat/', views.random_cat_picture, name='random_cat_picture')
]