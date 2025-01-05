"""
    **Поиск максимального и минимального элемента в списке:**
   - Напишите функцию, которая принимает список чисел и возвращает кортеж, содержащий минимальное и максимальное
   значения. Не используйте встроенные функции `max` и `min`.

"""


def max_min_numbers(numbers):
    """
    Функция принимает список чисел и возвращает кортеж, содержащий минимальное и максимальное значения.
    :param numbers: list of numbers
    :return: tuple of min and max numbers
    """
    max_number = numbers[0]
    min_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    return min_number, max_number


print(max_min_numbers([1, 2, 3, 12, 13, 14, 4, 5, 6, 18, 7, 8, 9, 10]))
