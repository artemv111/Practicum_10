def fibonacci(n):
    '''
    Функция печатает первые n чисел последовательности Фибоначчи
    '''
    if n > 0:
        first, second = 1, 1
        print(first,end=' ')
        if n >= 2:
            print(second,end=' ')

        for _ in range(2, n):
            third = first + second
            print(third,end=' ')
            first, second = second, third

n = int(input())
fibonacci(n)
