import sqlite3


class History:
    """Historique des opérations stocké dans SQLite."""

    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS operations ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "expression TEXT NOT NULL, "
            "result REAL NOT NULL)"
        )
        self.conn.commit()

    def record(self, expression, result):
        self.conn.execute(
            "INSERT INTO operations (expression, result) VALUES (?, ?)",
            (expression, result),
        )
        self.conn.commit()

    def all(self):
        cursor = self.conn.execute(
            "SELECT expression, result FROM operations ORDER BY id"
        )
        return cursor.fetchall()

    def close(self):
        self.conn.close()