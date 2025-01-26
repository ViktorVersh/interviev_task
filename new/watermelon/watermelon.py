def div_even(n) -> str:
    """
    Функция проверяет, чётное ли число.
    :param n:
    :return: возвращает строку если четное и больше 2 "YES", иначе "NO"
    """
    if n > 2 and n % 2 == 0:
        return "YES"
    else:
        return "NO"


try:
    a_wight = int(input("Введите любое целое число от 1 до 100 включительно: "))
    if 1 <= a_wight <= 100:
        print(div_even(a_wight))
    else:
        print("Error")  # если введено число вне диапазона от 1 до 100
except ValueError as er:
    print("Error")  # если введено не целое число
