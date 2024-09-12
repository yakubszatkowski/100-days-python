from .models import Favorite

def cat_favorite_ajax_post_request(response):
    task = response.POST.get('task')
    cat_id =  response.POST.get('cat_id')
    
    if task == 'true':
        fav_cat = Favorite(favorite_cat_id=cat_id)
        fav_cat.save()
        response.user.favoritelist.add(fav_cat)
    elif task == 'false':
        fav_cat_to_delete = Favorite.objects.get(user=response.user, favorite_cat_id=cat_id)
        fav_cat_to_delete.delete()


def cat_favorite_user_request(response):
    return Favorite.objects.filter(user=response.user)


# http://127.0.0.1:8000/cat/qg0_IodJp