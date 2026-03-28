P = int(input())

def make_payment(P):
    if P >= 20 and P <= 1000:
        print('Успех')
    else:
        print('Повторить попытку')

make_payment(P)