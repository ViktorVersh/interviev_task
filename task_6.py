"""
Задание 6: Поиск максимального элемента в списке

Описание: Напишите функцию, которая принимает список чисел и возвращает максимальный элемент.

Вход: Список целых чисел (например, 3, 5, 2, 9, 1)

Выход: Целое число — максимальный элемент списка (например, 9).

Пример:

def find_max(numbers: list) -> int:
    # Ваша реализация
"""


def find_max(numbers: list) -> int:
    return max(numbers)


numbers_list = [3, 5, 2, 9, 1, 8, 10, 15]
print(find_max(numbers_list))