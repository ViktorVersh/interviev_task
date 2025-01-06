"""
    Чтение и запись файла:
    - Напишите программу, которая считывает содержимое текстового файла и записывает его в новый файл в верхнем
    регистре. Если исходный файл не существует, программа должна вывести сообщение об ошибке
"""


def rewrite_file(file_name):
    """
    Функция, которая считывает содержимое текстового файла и записывает его в новый файл в верхнем регистре.
    :param file_name:
    :return:
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            with open(file_name + '_upper', 'w', encoding='utf-8') as file_upper:
                file_upper.write(text.upper())
    except FileNotFoundError as error:
        print(error)
    return


rewrite_file('test_file.txt')
