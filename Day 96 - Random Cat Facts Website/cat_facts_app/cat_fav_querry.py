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
    user_favorites = Favorite.objects.filter(user=response.user)
    return [id.favorite_cat_id for id in user_favorites]


def is_cat_favorite(response, cat_id):
    user_favorite_cats_ids = cat_favorite_user_request(response)
    if cat_id in user_favorite_cats_ids:
        return True
    else:
        return False


# http://127.0.0.1:8000/cat/qg0_IodJp