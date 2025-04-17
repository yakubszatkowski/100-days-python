import os
import smtplib
import datetime as dt
from random import choice

g_mail = 'rtyrtyqweqwe39@gmail.com'
yahoo_mail = 'qweqwe.rtyrty@yahoo.com'
gmail_app_password = os.environ.get('D32_gmail_app_pass')

with open('quotes.txt', 'r') as quotes:
    quote_list = quotes.readlines()

now = dt.datetime.now()
today_weekday = now.weekday()
random_quote = choice(quote_list)

if today_weekday == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(g_mail, gmail_app_password)
        connection.sendmail(
            g_mail, yahoo_mail,
            msg='Subject: Motivational quote of today'
                f'\n\n {random_quote}'
        )
