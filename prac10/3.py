

def discount(price, discount_card, holiday):

    discount = 0
    if price > 30000:
        discount += 10
    elif price > 20000:
        discount += 7
    elif price > 15000:
        discount += 5
    elif price > 5000:
        discount += 3

    if discount_card:
        discount += 5
    if holiday:
        discount += 3

    if discount > 15:
        discount = 15

    return round(price * (100 - discount) / 100, 2)

print(discount(21000, True, True))