from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('random_cat/', views.random_cat_picture, name='random_cat_picture'),
    path('random_cat_breed/', views.random_cat_picture_by_breed, name='random_cat_picture_by_breed'),
    path('post_your_cat/', views.post_your_cat, name='post_your_cat')
]