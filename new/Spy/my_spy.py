def find_index(arr):
    """
    Функция находит индекс элемента, встречающегося один раз в массиве.
    :param arr: Принимает массив
    :return: Индекс элемента, встречающегося один раз в массиве (нумерация с единицы)
    """
    frequency = {}
    for i in arr:
        frequency[i] = frequency.get(i, 0) + 1  # Подсчёт частоты каждого элемента
    for j in arr:
        if frequency[j] == 1:
            return arr.index(j) + 1  # Нахождение уникального элемента (индексация с единицы)


# Чтение входных данных
t = int(input("Введите количество тестов: "))
results = []

for _ in range(t):
    n = int(input("Введите размер массива: "))
    array = list(map(int, input("Введите через пробел массив: ").split()))

    result = find_index(array)

    results.append(result)

# Вывод результатов
for res in results:
    print(res)
