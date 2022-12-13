import os

import requests
import smtplib
import time
from datetime import datetime
email = 'yakub.szatkowski@gmail.com'
LAT = 50.318329
LNG = 19.070110
parameters = {
    'lat': LAT,
    'lng': LNG,
    'formatted': 0,
}

while True:
    # ISS API #
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    iss_position = (latitude, longitude)
    my_position = (LAT, LNG)

    # Sunrise/sunset API #
    response_sun = requests.get('https://api.sunrise-sunset.org/json', parameters)
    response_sun.raise_for_status()
    data = response_sun.json()['results']
    sunrise = data['sunrise']
    sunset = data['sunset']
    sunrise_time = int(sunrise.split('T')[1].split(':')[0])
    sunset_time = int(sunset.split('T')[1].split(':')[0])

    # Hour right now
    time_now = datetime.now().hour

    # if time is after sunrise or before sunset and satelite position is +- 5 degrees of your location latitude and
    # longitude it will e-mail you telling you to look up!
    if time_now >= sunset_time or time_now <= sunrise_time:
        if iss_position[1] - 5 <= my_position[1] <= iss_position[1] + 5 and iss_position[0]-5 <= my_position[0] <= \
                iss_position[0]+5:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user='rtyrtyqweqwe39@gmail.com', password=os.environ.get('D32_gmail_app_pass'))
                connection.sendmail(
                    from_addr='rtyrtyqweqwe39@gmail.com', to_addrs=email,
                    msg=f'Subject:Look up!\n\nThe ISS satellite is near you!'
                )
            print('e-mail sent!')
    time.sleep(60)