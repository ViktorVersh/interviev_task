"""
Задание 3: Факториал

Описание: Напишите функцию, которая рассчитывает факториал числа.

Вход: Целое число n (например, 5)

Выход: Целое число — факториал n (например, 120 для 5).

Пример:

def factorial(n: int) -> int:
    # Ваша реализация
"""


def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
