def Sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + (n-1) % 9
print(Sum_of_digits(589))