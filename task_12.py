"""
Задание 12: Проверка палиндрома

Описание: Напишите функцию, которая принимает строку и проверяет, является ли она палиндромом.

Вход: Строка (например, "racecar")

Выход: Логическое значение (True, если палиндром, иначе False).

Пример:

def is_palindrome(s: str) -> bool:
    # Ваша реализация
"""
def is_palindrome(s: str) -> bool:
    s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome('rac eca r '))
