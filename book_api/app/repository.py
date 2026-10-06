from .database import get_connection

class BookRepository:
    def add(self, title, author, year):
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year),
            )
            return cursor.lastrowid   #id новой строки


    def get_all(self, author=None, is_read=None):
        query = "SELECT id, title, author, year, is_read FROM books WHERE 1=1"
        params = []

        if author is not None:
            query += " AND author = ?"
            params.append(author)

        if is_read is not None:
            query += " AND is_read = ?"
            params.append(int(is_read))    #bool -> 0/1

        with get_connection() as conn:
            rows = conn.execute(query, params).fetchall()
            return [dict(row) for row in rows]


    def get_by_id(self, book_id):
        with get_connection() as conn:
            row = conn.execute(
                "SELECT id, title, author, year, is_read FROM books WHERE id = ?", (book_id,),
            ).fetchone()
            return dict(row) if row else None

    def update(self, book_id, title, author, year):
        with get_connection() as conn:
            conn.execute(
                "UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?", (title, author, year, book_id),
            )

    def delete(self, book_id):
        with get_connection() as conn:
            conn.execute("DELETE FROM books WHERE id = ?", (book_id,))

    def mark_as_read(self, book_id):
        with get_connection() as conn:
            conn.execute(
                "UPDATE books SET is_read = 1 WHERE id = ?", (book_id,),
            )