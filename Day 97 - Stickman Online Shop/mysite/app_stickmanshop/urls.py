from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('collection', views.collection, name='collection'),
    path('profile', views.profile, name='profile'),
    path('stickman/<str:id>', views.stickman, name="stickman"),
    # path('wrong_path',)
]