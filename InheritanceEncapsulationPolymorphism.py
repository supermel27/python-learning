#Наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} издает звук")

    def sleep(self):
        print(f"{self.name} спит")


#super() — вызов родительского метода
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name}: Гав!")

    def info(self):
        print(f"{self.name}, порода: {self.breed}")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: Мяу!")

dog = Dog('Бобик', 'корги')
cat = Cat('Барсик')
# dog.speak()
# cat.speak()
# dog.sleep()
# cat.sleep()
# dog.info()


#isinstance и issubclass
# print(isinstance(dog, Dog))
# print(isinstance(dog, Animal))
# print(issubclass(Dog, Animal))
# print(issubclass(Animal, Dog))


#Инкапсуляция
#Одно подчёркивание _attr — «не трогай, это внутреннее»
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # «защищённый» атрибут

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount

    def get_balance(self):
        return self._balance

b_a1 = BankAccount(1000)
b_a1.deposit(1000)
# print(b_a1.get_balance())

#_balance — соглашение: «это внутреннее, не обращайся снаружи напрямую». 
# Технически можно, но так делать не принято.


#Два подчёркивания __attr — «name mangling»
class User:
    def __init__(self, password):
        self.__password = password  #"приватный"

    def check_password(self, value):
        return self.__password == value

# user = User('secret')
# print(user.__password)         # AttributeError
# print(user._User__password)    # работает, но это уже «взлом»
# print(user.check_password('secret'))

#Это не настоящая защита, а сигнал: «не лезь». Используется редко.


#@property — геттеры и сеттеры по-питоновски
class Temperature:
    def __init__(self, cellsius):
        self._celsius = cellsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Ниже абсолютного нуля нельзя")
        self._celsius = value

t = Temperature(20)
# print(t.celsius)
# t.celsius = 25
# print(t.celsius)
# t.celsius = -300


#Полиморфизм
#Идея: разные классы могут иметь методы с одинаковым именем, 
# и работать с ними можно одинаково — не зная, какой именно класс перед тобой.
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав"

class Cat(Animal):
    def speak(self):
        return 'Мяу'

class Cow(Animal):
    def speak(self):
        return 'Му'

animals = [Dog(), Cat(), Cow()]
# for i in animals:
#     print(i.speak())


#Абстрактные методы
#Иногда хочется обязать наследников реализовать метод:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
        def speak(self):
            return "Гав"

class Fish(Animal):    #забыли speak
        pass

dog = Dog()
dog.speak()
# fish = Fish()

#ABC — абстрактный базовый класс. 
# Если наследник не реализует speak — объект нельзя создать. Это контракт: «любой Animal умеет говорить».


#Пример: система платежей
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def receipt(self):
        print(f"Оплата на {self.amount} руб. проведена")


class CardPayment(Payment):
    def pay(self):
        print(f"Оплата картой на {self.amount} руб.")

class CryptoPayment(Payment):
    def pay(self):
        print(f"Оплата криптой на {self.amount} руб.")

payments = [CardPayment(1000), CryptoPayment(500)]

for p in payments:
    p.pay()
    p.receipt()
    print("---")