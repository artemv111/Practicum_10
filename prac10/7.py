def NOK(a, b, n):
    for number in range(max(a,b), n+1):
        if number % a == 0 and number % b == 0:
            print(number, end=' ')

NOK(7,2,100)


