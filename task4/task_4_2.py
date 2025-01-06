"""
    Подсчет строк в файле:
    - Создайте функцию, которая принимает имя текстового файла и возвращает количество строк в этом файле.
    Убедитесь, что функция обрабатывает возможные ошибки, такие как отсутствие файла.
"""


def count_lines(file_name):
    """
    Функция подсчёта строк в файле используя функцию len()
    :param file_name:
    :return: len(file.readlines())
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return len(file.readlines())
    except FileNotFoundError as error:
        print('File not found', error)


# def count_lines(file_name):
#     """
#     Функция подсчёта строк в файле используя цикл for
#     :param file_name:
#     :return: count
#     """
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             count = 0
#             for i in file.readlines():
#                 count += 1
#             return count
#     except FileNotFoundError as error:
#         print('File not found', error)


print(count_lines('test.txt'))
