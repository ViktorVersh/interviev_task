def find_index(arr):
    """
    Функция находит индекс элемента, встречающегося один раз в массиве.
    :param arr: Принимает массив
    :return: Индекс элемента, встречающегося один раз в массиве (нумерация с единицы)
    """
    from collections import Counter
    count = Counter(arr)  # Создаем счетчик для подсчета частоты каждого числа
    unique_number = next(k for k, v in count.items() if v == 1)  # Находим число, которое встречается только один раз
    return arr.index(unique_number) + 1  # Возвращаем индекс этого числа в исходном массиве


# Чтение входных данных
t = int(input("Введите количество тестов: "))
results = []  # Создаем список для хранения результатов

for _ in range(t):  # Проходим циклом по всем тестам
    n = int(input("Введите размер массива: "))
    array = list(map(int, input("Введите через пробел массив: ").split()))

    result = find_index(array)  # Находим индекс уникального элемента

    results.append(result)  # Добавляем результат в список

# Вывод результатов
for i in results:
    print(i)
