import datetime

def format_weekday_text(opening_hours):
    weekday_info = {}
    for day in opening_hours:
        day = ''.join([char if ord(char) < 128 else ' ' for char in day])
        day = day.split(':', 1)
        split_list = [char for char in day[1].split(' ')]
        if 'Closed' in split_list:
            weekday_info[day[0]] = 'Closed'
        elif 'Open' in split_list:
            weekday_info[day[0]] = 'Open 24 hours'
        else:
            if 'AM' in split_list:
                day[1] = split_list[1], split_list[5]
            else:
                day[1] = split_list[1], split_list[4]
            day[1] = [datetime.datetime.strptime(time_string, '%H:%M').time() for time_string in day[1]]
            day[1][1] = (datetime.datetime.combine(datetime.date.today(), day[1][1]) + datetime.timedelta(hours=12)).time()
            weekday_info[day[0]] = day[1]
    
    today_weekday = datetime.datetime.today().strftime('%A')
    time_now = datetime.datetime.today().time()

    is_open = False
    for weekday, active_hours in weekday_info.items():
        if active_hours == 'Closed':
            pass
        elif active_hours == 'Open 24 hours':
            is_open = True
        else:
            if weekday == today_weekday:
                opening, closing = active_hours
                is_open = False
                if opening < closing:
                    if opening <= time_now <= closing:
                        is_open = True
                else:
                    if time_now >= opening or time_now <= closing:
                        is_open = True
            
            weekday_info[weekday] = [time.strftime('%H:%M') for time in active_hours]

    info = {
        'weekdays_opening_hours': weekday_info,
        'is_open': is_open
    }

    return info

