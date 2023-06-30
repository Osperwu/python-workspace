'''recursion 遞迴'''


# def factorial_loop(n):
#     factor = 1
#     for i in range(1, n + 1):
#         factor *= i
#     return factor
#
#
# f = factorial_loop(3)
# print(f)
#
# for i in range(6):
#     print(i, end="")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))
