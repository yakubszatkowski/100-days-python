# https://docs.google.com/spreadsheets/d/1-IX5xYzCXwkaCIvxxaSqCmXO3E4DoqaIWXFkXU3eOYg/edit#gid=1105789396
import smtplib
import requests
import os

sheety_username = os.environ.get('D39_sheety_username')
sheety_pass = os.environ.get('D39_basicauth_pass')
sheety_endpoint = f'https://api.sheety.co/{sheety_username}/kopiaFlightDeals/users'

get_data = requests.get(url=sheety_endpoint,
                        auth=(sheety_username, sheety_pass))
names_emails = get_data.json()['users']


class NotificationManager:
    def __init__(self):
        self.names_emails = names_emails

    def send(self, message):
        for name_email in self.names_emails:
            email = name_email['email']
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user='rtyrtyqweqwe39@gmail.com', password=os.environ.get('D32_gmail_app_pass'))
                connection.sendmail(
                    from_addr='rtyrtyqweqwe39@gmail.com', to_addrs=email,
                    msg=f'Subject: New flight deal! \n\n {message}')
