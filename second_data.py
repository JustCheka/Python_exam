from datetime import datetime

def show_time():
    today = datetime.now()
    format_date = today.strftime('дата = %Y.%m.%d, время = %H:%M:%S')

    day = today.strftime('%A')
    week = today.isocalendar()[1]

    print(format_date)
    print('День недели ' + str(day))
    print('Номер недели ' + str(week))

show_time()