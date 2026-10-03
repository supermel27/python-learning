#Задача 1. Функции-калькуляторы.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

print(add(5, 6))
print(subtract(23, 5))
print(multiply(34, 12))
print(divide(12, 0))
print(divide(978, 14))


#Задача 2. Проверка пароля.

def is_strong_password(password):
    return ( len(password) >= 8 and any(char.isdigit() for char in password) and 
        any(char.isupper() for char in password) and any(char.islower() for char in password) )
       

print(is_strong_password("qwerty"))      # False
print(is_strong_password("qwerty123"))   # False
print(is_strong_password("QWERTY123"))   #False
print(is_strong_password("Qwerty123"))   # True


#Задача 3. Статистика чисел.

def analyze(numbers):
    if not numbers:
        return None
    return {
        'min': min(numbers),
        'max': max(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'count': len(numbers),
        'even_count': len([i for i in numbers if i % 2 == 0])
    }
 
print(analyze([1,2,3,4,5,6,7,8,9,10]))
print(analyze([]))