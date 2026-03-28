def seconds_count(data):
    parts = data.split()
    date_part, time_part = parts
    month, day, year = map(int, date_part.split('/'))
    hour, minute, second = map(int, time_part.split(':'))

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_days = sum(days_in_month[:month - 1]) + (day -1)
    total_seconds = total_days * 86400 + hour * 3600 + minute * 60 + second

    return total_seconds
data = input()
print(seconds_count(data))



