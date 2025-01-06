"""
    Поиск слова в файле:
    - Напишите программу, которая запрашивает у пользователя слово и ищет его в заданном текстовом файле.
    Программа должна вывести количество вхождений этого слова и строки, в которых это слово встречается.
"""
import re


def find_words(file_name):
    """
    Функция, ищет в файле заданное слово и выводит количество вхождений этого слова и строки,
    в которых это слово встречается.
    :param file_name
    :return:
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            word = input('Введите слово: ')
            search_word = rf'\b{re.escape(word)}\b'
            word_count = 0
            word_lines = []
            for i, line in enumerate(file, start=1):
                count = re.findall(search_word, line)
                if count:
                    word_count += len(count)
                    word_lines.append(i)
            return f'Слово "{word}" встречается в файле {word_count} раз, в строках: {word_lines}'
    except FileNotFoundError as error:
        print('Файл не найден', error)
        return


print(find_words('test_file.txt'))
