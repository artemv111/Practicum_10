n = int(input())

def fibonacci(n):

    if n > 0:
        first, second = 1, 1
        print(first,end=' ')
        if n >= 2:
            print(second,end=' ')

        for _ in range(2, n):
            third = first + second
            print(third,end=' ')
            first, second = second, third

fibonacci(n)
