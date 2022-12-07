# The most popular module for requesting API
import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response codes starting from 1XX- informational, 2XX- success, 3XX- redirection,
# 4XX- client error, 5XX- server error

# # This will produce 200 code, if there would be a type on url that would end up being 404 (not found)
# print(response)
# print(response.status_code)
#
# # # Errors and exceptions
# # if response.status_code == 404:
# #     raise Exception('That resource doesn\'t exist')
# # elif response.status_code == 401:
# #     raise Exception('You are not authorised to access this')
#
# # or instead that:
# response.raise_for_status()

# Getting hands on data from API in .json format:
data = response.json()
# print(data)
