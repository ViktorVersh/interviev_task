"""
Задание 1: Проверка палиндрома

Описание: Напишите функцию, которая принимает строку и проверяет,
является ли она палиндромом (читается одинаково как слева направо, так и справа налево).

Вход: Строка (например, "А роза упала на лапу Азора")

Выход: Булевое значение (True или False).

Пример:

def is_palindrome(s: str) -> bool:
    # Ваша реализация
"""

def is_palindrome(s: str) -> bool:
    s = s.lower()
    a = [" ", "'", ","]
    for i in a:
        s = s.replace(i, "")
    if s == s[::-1]:
        return True
    else:
        return False


result = is_palindrome("А роза упала на лапу Азора")
print(result)

result = is_palindrome("Madam I'm Adam")
print(result)

result = is_palindrome("Madam")
print(result)

result = is_palindrome("Компьютер")
print(result)
