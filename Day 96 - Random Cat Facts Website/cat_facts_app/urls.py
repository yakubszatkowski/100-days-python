from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('random_cat/', views.random_cat_picture, name='random_cat_picture'),
    path('random_cat_breed/', views.random_cat_picture_by_breed, name='random_cat_picture_by_breed'),
    path('browse_cats/', views.browse_cats, name='browse_cats'),
    path('cat/<str:id>/', views.cat_by_id, name='cat'),
    path('favorites/', views.browse_favorite_cats, name='favorites'),
    path('<str:username>', views.user_profile, name='user_profile')
]