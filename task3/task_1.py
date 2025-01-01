"""
**Функция для подсчета слов в строке:**
- Напишите функцию, которая принимает строку и возвращает количество уникальных слов в этой строке.
Учтите, что слова должны быть нечувствительны к регистру.
"""


def count_words(string):
    """
    Функция для подсчета слов в строке.
    """
    count_word = 0
    s = [',', '.', '!', '?', ':', ';', '(', ')', '[', ']', '{', '}']
    for i in s:
        string = string.replace(i, '')
    string = string.lower().split()
    st = list(dict.fromkeys(string))
    for i in st:
        if i in st:
            count_word += 1

    return count_word


print(count_words("Здравствуй школа. Снова Школа! Каникулы закончились снова на учебу! Ура! Ура! Ура!"))
print(count_words("Hello world"))
print(count_words("привет привет ПРивет! Какой хороший день! Добрый День!"))
