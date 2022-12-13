import os

import pandas as pd
import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
today_month_day = (now.month, now.day)
birthdays = pd.read_csv('./birthdays.csv')
birthdays = birthdays.to_dict(orient='index')
letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

for index in birthdays:
    name = birthdays[index]['name']
    email = birthdays[index]['email']
    month = birthdays[index]['month']
    day = birthdays[index]['day']
    birth_month_day = (month, day)
    if birth_month_day == today_month_day:
        with open(f'./letter_templates/{choice(letters)}') as letter:
            letter_contents = letter.read()
            final_letter = letter_contents.replace('[NAME]', name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user='rtyrtyqweqwe39@gmail.com', password=os.environ.get('D32_gmail_app_pass'))
            connection.sendmail(
                from_addr='rtyrtyqweqwe39@gmail.com', to_addrs=email,
                msg=f'Subject:Happy Birthday!\n\n{final_letter}'
            )

# uploading to cloud so the code runs everyday
# sign up to pythonanywhere.com
# files > upload files
# consoles > bash
# in console type:
# $ python3 main.py (in this case)
# dashboard > tasks
# schedule task in UTC
# create task
