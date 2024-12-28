"""
Задание 9: Классификация чисел

Описание: Напишите функцию, которая принимает список чисел и возвращает два списка:
один с четными и другой с нечетными числами.

Вход: Список целых чисел (например, 1, 2, 3, 4, 5)

Выход: Два списка (например, (2, 4, 1, 3, 5)).

Пример:

def classify_numbers(numbers: list) -> tuple:
    # Ваша реализация
"""


def classify_numbers(numbers: list) -> tuple:
    """
    функция принимает список чисел и возвращает два списка
    с четными и нечетными числами в виде кортежа:
    :param numbers:
    :return: tuple: (четные, нечетные)
    """
    honest_numbers = []
    odd_numbers = []
    for i in numbers:
        if i % 2 == 0:
            honest_numbers.append(i)
        else:
            odd_numbers.append(i)
    return honest_numbers, odd_numbers


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(classify_numbers(numbers_list))
