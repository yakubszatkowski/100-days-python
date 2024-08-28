import requests, os

API_KEY = os.environ.get('cat_api_key')
headers = {'x-api-key': API_KEY}


# VIEW PICTURES
def get_random_cat_picture():  # in start.html
    params = {
        'size': 'med',
        'has_breeds': 'true'
    }
    response = requests.get(url='https://api.thecatapi.com/v1/images/search', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    return data[0]


def get_random_cat_picture_by_breed(breed_id):  # in start.html
    params = {
        'size': 'med',
        'has_breeds': 'true',
        'breed_id': breed_id
    }
        
    response = requests.get(url='https://api.thecatapi.com/v1/images/search', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    return data[0]


# USER'S PICTURES
def post_your_cat_picture():  # in start.html
    pass


def get_your_posted_cat_pictures():  # in start.html
    pass


def delete_your_posted_cat_picture():  # in posted_cats.html
    pass


# USER'S FAVORITE PICTURES
def post_favorite_cat_picture():  # both in random_cat.html and random_cat_breed.html
    pass


def get_favorite_cat_pictures():  # in profile.html
    pass


def delete_favorite_cat_pictures():  # in saved.html
    pass

