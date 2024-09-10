
def cat_favorite_ajax_post_request(response):
        task = response.POST.get('task')
        cat_id =  response.POST.get('cat_id')
        print(task, cat_id)