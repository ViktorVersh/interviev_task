"""
Задание 14: Сумма цифр числа

Описание: Напишите функцию, которая принимает целое число и возвращает сумму его цифр.

Вход: Целое число (например, 1234)

Выход: Целое число — сумма цифр (например, 10).

Пример:

def sum_of_digits(n: int) -> int:
    # Ваша реализация
"""


def sum_of_digits(n: int) -> int:
    sum_digits = 0
    n_str = str(n)
    for i in range(len(n_str)):
        sum_digits += int(n_str[i])
    return sum_digits


print(sum_of_digits(167))
