import requests, os

API_KEY = os.environ.get('cat_api_key')
headers = {'x-api-key': API_KEY}


def get_random_cat_picture():  
    params = {
        'size': 'med',
        'has_breeds': 'true'
    }
    response = requests.get(url='https://api.thecatapi.com/v1/images/search', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    return data[0]


def get_random_cat_picture_by_breed(breed_id):  
    params = {
        'size': 'med',
        'has_breeds': 'true',
        'breed_id': breed_id
    }
    response = requests.get(url='https://api.thecatapi.com/v1/images/search', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    return data


def browse_random_cats(): 
    params = {
        'size': 'med',
        'has_breeds': 'true',
        'limit': 20
    }
    response = requests.get(url='https://api.thecatapi.com/v1/images/search', headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    print(data)
    return data


def show_cat_by_id(id):
    response = requests.get(url=f'https://api.thecatapi.com/v1/images/{id}')
    response.raise_for_status()
    data = response.json()

    return data

def favorite_cat_convert_ids_to_data(ids):
    cat_list = []
    for id in ids:
        response = requests.get(url=f'https://api.thecatapi.com/v1/images/{id}')
        cat_list.append(response.json())

    return cat_list
