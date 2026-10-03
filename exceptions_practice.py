import json
from datetime import datetime 
import time

#Задача 1. Безопасный ввод числа.

def safe_input_number(prompt):
    while True:
        value = input(prompt)
        if value.strip().lower() == 'exit':
            return None
        try:
            return int(value)
        except ValueError:
            print('It is not a number. Try again.')


# result = safe_input_number('Enter number: ')
# if result is None:
#     print('Выход')
# else:
#     print(f"Ты ввел число: {result}")
            
            
#Задача 2. Запись и чтение заметок.
def load_notes():
    try:
        with open("notes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open("notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def add_note(text):
    notes = load_notes()
    # notes.append(text)
    note = {
        'text': text,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes.append(note)
    save_notes(notes)

def delete_note(i):
    notes = load_notes()
    if not notes:
        print('Заметок нет')
        return
    if i < 1 or i > len(notes):
        print('Заметки с таким номером не существует')
        return
    notes.pop(i - 1)
    save_notes(notes)


def show_notes():
    notes = load_notes()
    if not notes:
        print('Заметок нет')
        return
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['created_at']} {note['text']}")

# add_note('Buy bread')
# add_note('Call mom')
# time.sleep(60)
# add_note('Read a chapter Python')
# # delete_note(1)
# delete_note(2)
# # delete_note(3)
# show_notes()


#Задача 3. Калькулятор с исключениями

def calculate(a, b, op):

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("В качестве аргументов можно использовать только числовые значения")
    if op not in ['+', '-', '*', '/', '**']:
        raise ValueError('Неизвестная операция')
    if b == 0 and op == '/':
        raise ZeroDivisionError('На ноль делить нельзя')
        
    if op == "+":
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '**':
        return a ** b

def run(a,b,op):
    try:
        result = calculate(a,b,op)
        print(result)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)

run(10, '2', "+")     # 12
run(10, 2, "-")
run(10, 2, "/")     # 5.0
run(10, 2, "*")
run(10, 2, "**")
run(10, 0, "/")     # На ноль делить нельзя
run(10, 2, "%")     # Неизвестная операция
run("10", 2, "+")
run("abc", 0, "/")




