class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greet(self):
        print(f"Hello, {self.name}")

    def speak(self, message):
        print(f"{self.name}: {message}")

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"User({self.name}, {self.age})"

user1 = User('Alex', 23, 'a@mail.com')  
# user1.greet()

# user2 = User('Sergei', 23, 's@mail.ru')
# user2.greet()

# print(user1.name)
# print(user1.age)
# print(user2.is_adult())
# user2.speak('hello!')
# print(user1)

#class bankAccount

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print('Сумма должна быть положителльной')
            return
        self.balance += amount
        print(f"Пополнено на {amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостаточно средств')
            return
        self.balance -= amount
        print(f"Снято {amount}. Баланс: {self.balance}")

    def show_balance(self):
        print(f"Счет {self.owner}: {self.balance} руб.")


# account = BankAccount('Alex', 1000)
# account.show_balance()
# account.deposit(1500)
# account.withdraw(700)
# account.withdraw(900)
# account.show_balance()

#наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('...')

class Dog(Animal):
    def speak(self):
        print(f"{self.name}: Гав!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}: Мяу!")

# dog = Dog('Bobik')
# cat = Cat('Barsik')
# dog.speak()
# cat.speak()


#Задача 1. Класс Book.
class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = False
    
    
    def info(self):
        print(f"Автор: {self.author}, Название: {self.title}, Год: {self.year}")

    def mark_as_read(self):
        self.is_read = True
        print('Книга отмечена как прочитанная')

    def age_of_book(self, current_year):
        return f"Книге {self.title} {current_year - self.year} лет"


book1 = Book('Snuff', 'Pelevin', 2011)
book1.info()
print(book1.is_read)
book1.mark_as_read()
print(book1.is_read)
print(book1.age_of_book(2026))

book2 = Book('Blue Lard', 'Sorokin', 1999)
book2.info()
print(book2.is_read)
book2.mark_as_read()
print(book2.is_read)
print(book2.age_of_book(2026))



#Задача 2. Класс Student с оценками.
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def show_grades(self):
        print(f"Оценки: {self.grades}")

    def __str__(self):
        return f"Student({self.name}, средний балл: {self.average()})"

    def is_excellent(self):
        return self.average() >= 4.5


student = Student("Сергей")
student.add_grade(5)
student.add_grade(4)
student.add_grade(5)
student.show_grades()       # Оценки: [5, 4, 5]
print(student.average())    # 4.666...
print(student.is_excellent())
print(student)              # Student(Сергей, средний балл: 4.666...)

