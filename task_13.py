"""
Задание 13: Подсчет гласных

Описание: Напишите функцию, которая принимает строку и подсчитывает количество гласных букв.

Вход: Строка (например, "hello world")

Выход: Целое число — количество гласных (например, 3).

Пример:

def count_vowels(s: str) -> int:
    # Ваша реализация
"""


def count_vowels(s: str) -> int:
    count = 0
    vowels = set('eyuioaуеыаояиюэё')
    for i in s:
        if i in vowels:
            count += 1
    return count


s = 'Здравствуй мир'
print(f'количество гласных: {count_vowels('Hello world')}')
print(f'количество гласных: {count_vowels('Здравствуйте мы снова вместе')}')
print(count_vowels(s))
