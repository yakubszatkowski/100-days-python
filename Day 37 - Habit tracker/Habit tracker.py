import requests
from datetime import datetime
TOKEN = 'ofenwa321iojdadsWQEkdso'
USERNAME = 'jacobjacob2222'
graph_id = 'jacobsgraph'
pixela_endpoint = 'https://pixe.la/v1/users'
headers = {
    'X-USER-TOKEN': TOKEN
}

today = datetime.now()
how_many_km = input('How many kilometers did you cycle today? ')
post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}'

post_pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': how_many_km,
}
response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)