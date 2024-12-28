"""
Задание 8: Ошибка в списке

Описание: Напишите функцию, которая принимает список целых чисел от 1 до n, но одно число отсутствует.
Найдите это число.

Вход: Список целых чисел (например, 1, 2, 4, 5, n=5)

Выход: Отсутствующее число (например, 3).

Пример:

def find_missing_number(numbers: list, n: int) -> int:
    # Ваша реализация
"""


def find_missing_number(numbers: list, n: int) -> int:
    for i in range(1, n + 1):
        if i not in numbers:
            return i


numbers = [1, 2, 4, 5]
print(find_missing_number(numbers, 5))
