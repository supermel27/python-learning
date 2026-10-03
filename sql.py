import sqlite3

#SQLite в Python


# Подключение (файл создастся автоматически)
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE users")
#Создание таблицы
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     age INTEGER
#     )
# """)

# Вставка — БЕЗОПАСНО через параметры
# cursor.execute(
#     "INSERT INTO users (name, email, age) VALUES (?,?,?)", ("Alex", "a@mail.ru", 35),
# )

# Несколько сразу
# cursor.executemany(
#     "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
#     [
#         ("Dick", "d@mail.ru", 32),
#         ("Mary", "m@mail.ru", 23)
#     ],
# )

# сохранить изменения
# conn.commit()

# Выборка
# cursor.execute("SELECT id, name, age FROM users WHERE age > ?", (25,))
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# conn.close()   #закрываем соединение


#SQL-инъекции — критически важно
#Никогда не подставляй данные в SQL через f-строку.

# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("O'Brien", "b@mail.ru"))

# cursor.execute("DELETE FROM users WHERE id > 3")
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("O'Brien", "b@mail.ru"))
# cursor.execute("UPDATE users SET age = 33 WHERE id = 31")
# cursor.execute("SELECT * FROM users") 
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


#Транзакции
# conn = sqlite3.connect("app.db")
# try:
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Jack", "j@mail.com"))
#     cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Ronald", "r@mail.com"))
#     conn.commit()   #фиксируем все
# except Exception as e:
#     conn.rollback()    #откатываем все
#     print(f"Ошибка: {e}")
# finally:
#     conn.close()

#Транзакция — группа операций «всё или ничего». 
# Если что-то упало — база возвращается к состоянию до начала. 
# Это критично для переводов денег, заказов и т.д.


#Класс-обёртка для БД
class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER
                )
            """)

    def add(self, name, email, age):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO users (name, email, age) VALUES (?,?,?)", (name, email, age),
            )

    def get_all(self):
        with self._connect() as conn:
            cursor = conn.execute("SELECT id, name, email, age FROM users")
            return cursor.fetchall()

    def find_by_age(self, min_age):
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, name, email, age FROM users WHERE age >= ?", (min_age,),
            )
            return cursor.fetchall()

    def delete(self, user_id):
        with self._connect() as conn:
            conn.execute("DELETE FROM users WHERE id = ?", (user_id,))


repo = UserRepository("app.db")
repo.create_table()
repo.add("Alex", "a@mail.com", 35)
repo.add('Serg', "s1mail.com", 33)
repo.add("Mary", "m@mail.com", 28)

print(repo.get_all())
print(repo.find_by_age(30))

    