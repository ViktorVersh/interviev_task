"""
    Запись и чтение JSON файла:
    - Создайте программу, которая считывает данные из текстового файла (каждая строка содержит информацию о
    человеке: имя, возраст, город) и сохраняет эти данные в JSON файл. Затем загрузите этот JSON файл и выведите
    список людей, отфильтровав по городу.
"""

import json


def copy_to_json(filename):
    """
    Функция копирует данные из текстового файла в JSON файл
    :param filename
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.readlines()
    with open('test_file.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_from_json(filename):
    """
    Функция загружает данные из json файла и выводит список людей, отфильтровав по городу
    :param filename:
    :return:
    """
    with open(filename, 'r') as file:
        data = json.load(file)
        city = input('Введите город: ')
        for i in data:
            if city.lower() in i.lower():
                print(i)
            else:
                continue
        return data


copy_to_json('test_file.txt')
load_from_json('test_file.json')
