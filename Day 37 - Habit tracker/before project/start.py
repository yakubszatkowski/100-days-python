import os

import requests
from datetime import datetime

# Not really a project more of learning stuff

# .get() request is made where we ask system for piece of data
# .post() request is where we give external system some piece of data idc about response
# .put() updating data in external service
# .delete() deleting data in external service

TOKEN = os.environ.get('D37_token')
USERNAME = 'jacobjacob2222'

# posting request for creating profile (https://pixe.la/@jacobjacob2222)
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# # Two lines below are used only once to create the account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_configuration = {
    'id': 'jacobsgraph',
    'name': 'Cycling graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai',
}
# No token in parameters instead this:
headers = {
    'X-USER-TOKEN': TOKEN
}
# # Line below creates a graph, needs to be used once
# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)

# # Lines below are putting pixel onto the graph
today = datetime.now()
how_many_km = input('How many kilometers did you cycle today? ')
post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_configuration["id"]}'
post_pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': how_many_km,
}
response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)

# # Editing/updating the pixel from the graph
# put_pixel_config = {
#     'quantity': '10.5'
# }
# put_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_configuration["id"]}/{today.strftime("%Y%m%d")}'
# response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
# print(response.text)

# # Deleting the pixel from the graph
# delete_pixel_config = {
#     None
# }
# delete_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_configuration["id"]}/{today.strftime("%Y%m%d")}'
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
