"""
**Сортировка списка слов по длине:**
- Создайте функцию, которая принимает список строк, а затем возвращает новый список, отсортированный
по длине слов, начиная с самых коротких.
"""


def new_list(list_string):
    list_string.sort(key=len)
    return list_string


print(new_list(["hello", "world", "python", "is", "great", "the", "pie", "apple"]))
