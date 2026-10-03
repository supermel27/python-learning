#Задача 1. Фигуры.
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"{self.name}: площадь {self.area()}, периметр {self.perimeter()}")

    def is_larger_than(self, other):
        return self.area() > other.area()


class Rectangle(Shape):
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


class Circle(Shape):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def perimeter(self):
        return self.a + self.b + self.c


rect = Rectangle('rectangle', 4, 5)
cir = Circle('circle', 5)
tr = Triangle('triangle', 3,4,5)

shapes = [rect, cir, tr]
for shape in shapes:
    shape.describe()

print(rect.is_larger_than(cir))
print(cir.is_larger_than(tr))
print(tr.is_larger_than(rect))


#Задача 2. Сотрудники.
class Employee:
    BONUS_RATE = 0
    position = ''

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        

    def info(self):
        print(f"{self.name}: должность - {self.position}, оклад - {self.salary}, бонус - {self.get_bonus()}")

    def get_bonus(self):
        return self.BONUS_RATE * self.salary

    def total_income(self):
        return self.salary + self.get_bonus()

    
class Manager(Employee):
    BONUS_RATE = 0.2
    position = 'manager'

class Developer(Employee):
    BONUS_RATE = 0.1
    position = 'developer'

class Intern(Employee):
    position = 'intern'

class SalesManager(Employee):
    BONUS_RATE = 0.3
    position = 'sales manager'

manager = Manager('Alex', 1500)
dev = Developer ('Nick', 1300)
intern = Intern('Dick', 800)
sale = SalesManager('Jack', 2000)


employees = [manager, dev, intern, sale]
for employee in employees:
    employee.info()
    print(f"Бонус: {employee.get_bonus()}")
    print(f"Итого: {employee.total_income()}")

