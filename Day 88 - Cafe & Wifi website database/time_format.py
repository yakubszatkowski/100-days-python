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
                time_elements = f'{split_list[1]} {split_list[2]}', f'{split_list[5]} {split_list[6]}'
            else:
                time_elements = f'{split_list[1]} {split_list[5]}', f'{split_list[4]} {split_list[5]}'
            time_elements = [datetime.datetime.strptime(time_string, '%I:%M %p').time() for time_string in time_elements]
            weekday_info[day[0]] = time_elements
    
    # print(weekday_info)
    
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

# # TESTING
# opening_hours = [
#   'Monday: 12:00\u2009–\u200910:00\u202fPM',
#   'Tuesday: 2:00\u2009–\u20098:00\u202fPM',
#   'Wednesday: 10:00\u202fAM\u2009–\u200910:00\u202fPM',
#   'Thursday: 10:00\u202fAM\u2009–\u200910:00\u202fPM',
#   'Friday: 10:00\u202fAM\u2009–\u200911:00\u202fPM',
# #   'Saturday: 10:00\u202fAM\u2009–\u200911:00\u202fPM',
# #   'Sunday: 10:00\u202fAM\u2009–\u200911:00\u202fPM'
#   'Saturday: Open 24 hours',
#   'Sunday: Closed'
# ]

# x = format_weekday_text(opening_hours)
# print(x)