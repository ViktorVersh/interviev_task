"""
Задание 10: Удаление дубликатов

Описание: Напишите функцию, которая принимает список и удаляет все дубликаты, оставляя уникальные значения.

Вход: Список (например, 1, 2, 2, 3, 4, 4, 5)

Выход: Список уникальных значений (например, 1, 2, 3, 4, 5).

Пример:

def remove_duplicates(numbers: list) -> list:
    # Ваша реализация
"""


def remove_duplicates(numbers: list) -> list:
    return list(set(numbers))


numbers_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers_list))
