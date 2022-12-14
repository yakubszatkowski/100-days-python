import smtplib
import os


class NotificationManager:
    def send(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user='rtyrtyqweqwe39@gmail.com', password=os.environ.get('D32_gmail_app_pass'))
            connection.sendmail(
                from_addr='rtyrtyqweqwe39@gmail.com', to_addrs='yakub.szatkowski@gmail.com',
                msg=f'Subject: New flight deal! \n\n {message}'
            )
