"""
Задание 15: Упорядочение слов в строке
Описание: Напишите функцию, которая принимает строку и возвращает её, где слова упорядочены по их длине.
Вход: Строка (например, "the quick brown fox")
Выход: Строка с упорядоченными словами (например, "the fox quick brown").
Пример:

def sort_words_by_length(s: str) -> str:
    # Ваша реализация
"""


def sort_words_by_length(s: str) -> str:
    words = s.split()
    print(words)
    words.sort(key=lambda x: len(x))
    print(words)
    return ' '.join(words)


print(sort_words_by_length("Здравствуйте вот мы и встретились снова"))
