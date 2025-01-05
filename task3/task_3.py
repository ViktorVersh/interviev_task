"""
    **Класс "Круг":**
   - Реализуйте класс `Circle`, который имеет атрибут радиуса. Класс должен содержать методы для вычисления
   площади и периметра круга. Площадь = π * r^2, Периметр = 2 * π * r.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def square(self):
            return self.pi * self.radius ** 2

    def perimetr(self):
        return round(2 * self.pi * self.radius, 2)

    def __str__(self):
        return f'Площадь круга = {self.square()}, Периметр круга = {self.perimetr()}'


r1 = Circle(int(input('Введите радиус круга: ')))
print(r1)
