"""
Задание 4: Фильтрация четных чисел

Описание: Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий только четные числа.

Вход: Список целых чисел (например, 1, 2, 3, 4, 5)

Выход: Список четных чисел (например, 2, 4).

Пример:

def filter_even_numbers(numbers: list) -> list:
    # Ваша реализация
"""


def filter_even_numbers(numbers: list) -> list:
    return [i for i in numbers if i % 2 == 0]


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_numbers(numbers_list))
