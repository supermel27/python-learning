import sqlite3

class BookRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL, 
                    author TEXT NOT NULL,
                    year INTEGER,
                    is_read INTEGER DEFAULT 0
                )
            """)

    def add(self, title, author, year):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO books (title, author, year) VALUES (?,?,?)", (title, author, year),
            )

    def get_all(self):
        with self._connect() as conn:
            cursor = conn.execute("SELECT id, title, author, year, is_read FROM books")
            return cursor.fetchall()

    def mark_as_read(self, book_id):
        with self._connect() as conn:
            conn.execute(
                "UPDATE books SET is_read = 1 WHERE id = ?", (book_id,),
            )

    def find_unread(self):
        with self._connect() as conn:
            cursor = conn.execute("SELECT id, title, author, year, is_read FROM books WHERE is_read = 0")
            return cursor.fetchall()  

    def find_by_author(self, author):
        with self._connect() as conn:
            cursor = conn.execute("SELECT id, title, author, year, is_read FROM books WHERE author = ?", (author,))
            return cursor.fetchall()

    def delete(self, book_id):
        with self._connect() as conn:
            conn.execute("DELETE FROM books WHERE id = ?", (book_id,))

    def count_by_year(self, year):
        with self._connect() as conn:
            cursor = conn.execute("SELECT COUNT(*) FROM books WHERE year = ?", (year,))
            return cursor.fetchone()[0]

    def drop_table(self):
        with self._connect() as conn:
            conn.execute("DROP TABLE books")


# repo = BookRepository("app2.db") 
# repo.drop_table()   
# repo.create_table()
# repo.add("Snuff", "Pelevin", 2011)
# repo.add("Three sisters", "Chehov", 1901)
# repo.add("Novel", "Sorokin", 2011)
# repo.add("Suitcase", "Dovlatov", 1978)
# repo.mark_as_read(1)    
# print(repo.get_all())
# print(repo.find_unread())
# print(repo.count_by_year(2011))
# print(repo.find_by_author("Sorokin"))
# repo.delete(2)
# print(repo.get_all())


#Задача 2. Сотрудники.
class EmployeeRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary INTEGER NOT NULL
                    )
                """)

    def add(self, name, position, salary):
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO employees (name, position, salary) VALUES (?,?,?)", (name, position, salary),
                )

    def get_all(self):
        with self._connect() as conn:
            cursor = conn.execute("SELECT id, name, position, salary FROM employees")
            return cursor.fetchall()

    def get_by_position(self, position):
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, name, position, salary FROM employees WHERE position = ?", (position,)
                )
            return cursor.fetchall()

    def average_salary(self):
        with self._connect() as conn:
            cursor = conn.execute("SELECT AVG(salary) FROM employees")
            return cursor.fetchone()[0]

    def highest_paid(self):
        with self._connect() as conn:
            cursor = conn.execute("SELECT id, name, position, salary FROM employees ORDER BY salary DESC LIMIT 1")
            return cursor.fetchone()

    def raise_salary(self, position, percent):
        with self._connect() as conn:
            conn.execute(
                "UPDATE employees SET salary = salary + (salary * ? / 100) WHERE position = ?", (percent, position,)
                )

    def drop_table(self):
        with self._connect() as conn:
            conn.execute("DROP TABLE employees")


repo = EmployeeRepository("app3.db")
repo.drop_table()
repo.create_table()
repo.add("Alex", "DevOps", 5500)
repo.add("Dick", "Backend developer", 5000)
repo.add("John", "Frontend developer", 4500)
repo.add("Mary", "Project manager", 6000)
print(repo.get_all())
print(repo.get_by_position("DevOps"))
print(repo.average_salary())
print(repo.highest_paid())
repo.raise_salary("Frontend developer", 10)
print(repo.get_all())