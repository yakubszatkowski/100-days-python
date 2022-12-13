import smtplib
import datetime as dt
import os

g_mail = 'rtyrtyqweqwe39@gmail.com'
yahoo_mail = 'qweqwe.rtyrty@yahoo.com'
gmail_password = os.environ.get('D32_gmail_pass')
gmail_app_password = os.environ.get('D32_gmail_app_pass')
yahoo_password = os.environ.get('D32_yahoo_pass')  # yahoo app password currently doesn't work lol
smtp_yahoo = "smtp.mail.yahoo.com"
smtp_gmail = "smtp.gmail.com"

# # Option 1 - requiring closing at the end #
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=g_mail, password=gmail_app_password)
# connection.sendmail(
#     from_addr=g_mail, to_addrs=yahoo_mail,
#     msg='Subject:Hello\n\nThis is the body of my e-mail')
# connection.close()

# Option 2 #
with smtplib.SMTP(smtp_gmail) as connection:
    connection.starttls()
    connection.login(user=g_mail, password=gmail_app_password)
    connection.sendmail(
        from_addr=g_mail, to_addrs='yakub.szatkowski@gmail.com',
        msg='Subject:Hello\n\nThis is another e-mail'
    )

# # Getting date and time that is right now
# now = dt.datetime.now()
# year = now.year
# month = now.month
#
# # weekday starts counting from 0 which means 0 is monday, that is not the case in months
# todays_weekday = now.weekday()
# # print(todays_weekday)
#
# date_of_birth = dt.datetime(year=1994, month=8, day=30)
# print(date_of_birth)


# D32_gmail_passw=wQwerty123