"""
Создание словаря из файла:
- Реализуйте функцию, которая считывает текстовый файл, содержащий пары "ключ: значение" (по одному на строку),
и возвращает словарь, где ключами являются слова, а значениями — числа, представляющие количество вхождений
этих слов в файле.
"""

def file_to_dict(filename):
    """
    Функция, которая считывает текстовый файл, содержащий пары "ключ: значение" (по одному на строку),
    и возвращает словарь, где ключами являются слова, а значениями — числа, представляющие количество вхождений
    этих слов в файле.
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read()
        a = [':', ';', ',' '.', '!', '?']
        for i in a:
            words = words.replace(i, ' ')
        words = words.split()
    return {word: words.count(word) for word in words}


print(file_to_dict('test_file1.txt'))
