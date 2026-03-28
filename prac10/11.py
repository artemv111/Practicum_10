def is_prime(num):
    if num < 2:
        return 0
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0:
        return 1
    else:
        return 0

n = int(input())
for i in range(1, n + 1):
    if is_prime(i) == 1:
        print(i, end=" ")