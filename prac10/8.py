def data_print(data):
    try:
        parts = data.split()
        if len(parts) != 2:
            print('Неверные данные')
            return

        date_part, time_part = parts
        date = date_part.split('/')
        time = time_part.split(':')

        if len(date) != 3 or len(time) != 3:
            print('Неверные данные')
            return

        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        hour = int(time[0])
        minute = int(time[1])
        second = int(time[2])

        if month < 1 or month > 12:
            print('Неверные данные')
            return
        if day < 1 or day > 31:
            print('Неверные данные')
            return
        if hour < 0 or hour > 23:
            print('Неверные данные')
            return
        if minute < 0 or minute > 59:
            print('Неверные данные')
            return
        if second < 0 or second > 59:
            print('Неверные данные')
            return

        if hour == 0:
            hour_12 = 12
            am_pm = "AM"
        elif hour < 12:
            hour_12 = hour
            am_pm = "AM"
        elif hour == 12:
            hour_12 = 12
            am_pm = "PM"
        else:
            hour_12 = hour - 12
            am_pm = "PM"

        print(f"{month:02d}.{day:02d}.{year % 100:02d} {hour_12}:{minute:02d}:{second:02d} {am_pm}")

    except (ValueError, IndexError):
        print('Неверные данные')

date = input()
data_print(date)