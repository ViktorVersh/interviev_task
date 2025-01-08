"""
    Копирование файлов:
    - Реализуйте функцию для копирования содержимого одного текстового файла в другой. Убедитесь, что если
    целевой файл уже существует, программа предупреждает пользователя и предлагает перезаписать или отменить операцию.
"""
import os


def copy_file(source, target):
    """
    Функция копирования содержимого одного текстового файла в другой.
    :return:
    """
    try:
        with open(source, 'r', encoding='utf-8') as source_file:
            if os.path.exists(target):
                print('Файл уже существует. Перезаписать?')
                choice = input('y/n: ')
                if choice == 'y':
                    with open(target, 'w', encoding='utf-8') as target_file:
                        for line in source_file:
                            target_file.write(line)
                else:
                    print('Копирование отменено')
            else:
                with open(target, 'w', encoding='utf-8') as target_file:
                    for line in source_file:
                        target_file.write(line)
    except FileNotFoundError:
        print("Файл не найден")
    except IOError:
        print('Ошибка чтения файла')


copy_file('test.txt', "test_1.txt")
