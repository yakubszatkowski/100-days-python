import requests
import os

sheety_username = os.environ.get('D39_sheety_username')
sheety_pass = os.environ.get('D39_basicauth_pass')
sheety_endpoint = f'https://api.sheety.co/156480c5ea13a25cf378a0fd27983fd1/kopiaFlightDeals/users'


class User:
    def __init__(self):
        self.parameters = {}
        self.email_1 = ''
        self.email_2 = ''
        self.last_name = ''
        self.first_name = ''

    def add_user(self):
        self.first_name = input('What is your first name? \n')
        self.last_name = input('What is your last name? \n')
        self.email_1 = input('What is your email? \n')
        self.email_2 = input('Type your email again. \n')

        if self.email_1 == self.email_2:
            self.parameters = {
                'user': {
                    'firstName': self.first_name,
                    'lastName': self.last_name,
                    'email': self.email_1
                }
            }
            response_user_add = requests.post(url=sheety_endpoint,
                                              auth=(sheety_username, sheety_pass),
                                              json=self.parameters)
            print('You are in the club!')


User().add_user()

