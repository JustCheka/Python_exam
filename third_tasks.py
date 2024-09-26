from datetime import datetime, timedelta


def searching_date(days_from_now):
    today = datetime.now()
    search_date = today + timedelta(days=days_from_now)
    format_date = search_date.strftime('%Y.%m.%d')
    return format_date

days = int(input("Введите количество дней "))
print('Количество дней ' + str(days) + ', Искомая дата: ' + str(searching_date(days)))