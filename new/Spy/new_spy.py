def find_index(arr):
    frequency = {}
    for i in arr:
        frequency[i] = frequency.get(i, 0) + 1  # Подсчёт частоты каждого элемента
    for j in arr:
        if frequency[j] == 1:
            return arr.index(j) + 1  # Нахождение уникального элемента (индексация с единицы)


# Чтение входных данных
t = int(input())
results = []

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    result = find_index(array)

    results.append(result)

# Вывод результатов
for res in results:
    print(res)
