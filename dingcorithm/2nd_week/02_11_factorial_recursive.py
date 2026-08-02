def factorial(n):
    if n > 1:
        return factorial(n - 1) * n
    if n == 1:
        return 1


print(factorial(5))