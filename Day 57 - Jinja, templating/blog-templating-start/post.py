import requests


class Post:
    def __init__(self):
        self.response_blog = requests.get(url='https://api.npoint.io/2a276e24e4756cd30605').json()

