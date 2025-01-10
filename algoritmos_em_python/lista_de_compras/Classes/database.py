import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, text TEXT)''')

    def add_string(self, string):
        self.cursor.execute("INSERT INTO data (text) VALUES (?)", (string,))
        self.conn.commit()

    def get_all_strings(self):
        self.cursor.execute("SELECT text FROM data")
        rows = self.cursor.fetchall()
        return "\n".join(row[0] for row in rows)
    