from .models import FavoriteList

def cat_favorite_ajax_post_request(response):
        task = response.POST.get('task')
        cat_id =  response.POST.get('cat_id')
        
        if task == 'true':
            new_fav_cat = FavoriteList(favorite_cat_id=cat_id)
            new_fav_cat.save()
            response.user.favoritelist.add(new_fav_cat)