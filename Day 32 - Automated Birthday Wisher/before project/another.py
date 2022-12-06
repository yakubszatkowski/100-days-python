import smtplib

g_mail = 'rtyrtyqweqwe39@gmail.com'
gmail_password = 'wQwerty123'
gmail_app_password = 'ohkzrosqxtaybnso'
yahoo_mail = 'qweqwe.rtyrty@yahoo.com'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user='rtyrtyqweqwe39', password='ohkzrosqxtaybnso')
connection.sendmail(from_addr='rtyrtyqweqwe39@g_mail.com', to_addrs='qweqwe.rtyrty@yahoo.com',
                    msg='Subject:Hello\n\nThis is the body of my e-mail')
connection.close()
