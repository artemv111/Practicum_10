def print_numbers(a, b):
    if a > b:
        a, b = b, a

    allowed_digits = {'1', '3', '4', '8', '9'}

    for number in range(a, b + 1):
        for digit in str(number):
            if digit not in allowed_digits:
                break
        else:
            print(number, end=" ")

print(print_numbers(1,5676))