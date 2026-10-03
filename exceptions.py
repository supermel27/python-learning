import json

#2. try / except — перехват ошибок

# try:
#     number  = int(input('Enter number: '))
#     print(100 / number)
# except ValueError:
#     print('Это не число')
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# try:
#     number  = int(input('Enter number: '))
#     print(100 / number)
# except Exception as e:
#     print(f"Ошибка: {e}")

#Правило: перехватывай конкретные исключения. except Exception — крайняя мера, когда не знаешь, что может упасть.

#3. else и finally
# try:
#     number  = int(input('Enter number: '))
# except ValueError:
#     print("Это не число")
# else:
#     print(f"Ты ввел {number}")     #если не было ошибки
# finally:
#     print("Прогорамма завершилась")   #выполнится всегда


#4. raise — выбросить исключение самому
def check_age(age):
    if age < 0:
        raise ValueError("Возраст не может быть отрицаательным")
    return age

# print(check_age(4))


#5. Основные типы исключений
# Исключение	Когда возникает
# ValueError	Неверное значение: int("abc")
# TypeError	    Неверный тип: "2" + 2
# KeyError	    Нет ключа в словаре: d["no_key"]
# IndexError	Нет индекса в списке: lst[100]
# ZeroDivisionError	Деление на ноль
# FileNotFoundError	Файл не найден
# AttributeError	Нет атрибута/метода


#6. Работа с файлами

#Запись:
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!\n")
    f.write("Second line\n")

#Чтение:
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    # print(content)

#Чтение построчно:
# with open('hello.txt', 'r', encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

#Чтение всех строк в список:
# with open('hello.txt', 'r', encoding="utf-8") as f:
#     lines = f.readlines()
#     # print(lines)


#7. Файлы с исключениями
# try:
#     with open("no_file.txt", "r", encoding="utf-8") as f:
#         content = f.read()
# except FileNotFoundError:
#     print("Файл не найден")


#8. JSON — формат обмена данными
data = {
    "name": "Alex",
    "age": 35,
    "skills": ["python", "sql"]
}

# Записать в файл
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

#Прочитать из файла
with open("user.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

# print(loaded["name"])
# print(loaded["skills"])


#Преобразование без файла:
json_str = json.dumps(data, ensure_ascii=False)     #dict -> строка json
parsed = json.loads(json_str)                       #строка json -> dict

# print(json_str)
# print(parsed)


#9. Полный пример: TODO-лист
def load_todos():
    try:
        with open("todos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open("todos.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def main():
    todos = load_todos()

    while True:
        command = input("Команда (add/list/exit): ").strip().lower()

        if command == 'add':
            text = input("Что добавить? ")
            todos.append({"text": text, "done": False})
            save_todos(todos)
            print("Добавлено")

        elif command == "list":
            if not todos:
                print("Список пуст")
            for i, todo in enumerate(todos, 1):
                mark = "v" if todo['done'] else " "
                print(f"{i}. [{mark}] {todo['text']}")

        elif command == 'exit':
            break
        else:
            print("Неизвестная команда")

main()