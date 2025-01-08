"""
    Объединение файлов:
    - Напишите программу, которая принимает список текстовых файлов и объединяет их содержимое в один новый файл.
    Каждое содержимое файла должно быть отделено пустой строкой.
"""


def unite_files(*files):
    """
    Функция объединения файлов
    :param files:
    :return:
    """
    with open('result_test.txt', 'w') as result:
        for file in files:
            with open(file, 'r') as f:
                result.write(f.read())
                result.write('\n' '\n')
    return 'result_test.txt'


unite_files('test1.txt', 'test2.txt', 'test3.txt')
