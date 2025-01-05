"""
    **Генерация паролей:**
   - Напишите программу, которая генерирует случайные пароли заданной длины, используя буквы верхнего и
   нижнего регистра, цифры и специальные символы.
"""
import random


def generate_password(length):
    """
    Генерация пароля заданной длины
    :param length: длина пароля
    :return: пароль
    """
    password = ''
    for i in range(length):
        password += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnjhqrstuvwxyz1234567890!@#$%^&*')
    return password


print(generate_password(8))
