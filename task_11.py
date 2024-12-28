"""
Задание 11: Фибоначчи

Описание: Напишите функцию, которая принимает целое число n и возвращает n-й элемент последовательности Фибоначчи.

Вход: Целое число n (например, 5)

Выход: Целое число — n-й элемент последовательности (например, 5).

Пример:

def fibonacci(n: int) -> int:
    # Ваша реализация
"""
# import sys

# sys.set_int_max_str_digits(1000000)


# def fibonacci(n: int) -> int:
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(35))


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib(10))
