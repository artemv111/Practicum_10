value = int(input())

def card(value):
    if value == 25:
        value += 3
        return value
    elif value == 50:
        value += 8
        return value
    elif value == 100:
        value += 20
        return value
    else:
        return 'Недопустимая стоимость карты'

print(card(value))
