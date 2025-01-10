import sqlite3
from tkinter import messagebox

class User:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                administrador INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    try:
        def insert_user(self, name, password, administrador):
            self.cursor.execute('''
                INSERT INTO users (name, password, administrador)
                VALUES (?, ?, ?)
            ''', (name, password, administrador))
            self.connection.commit()
    except ValueError:
        messagebox.showinfo("Erro","Erro na função de inserir usuário!")

    try:
        def user_exists(self, name, password):
            self.cursor.execute('SELECT * FROM users WHERE name = ? AND password = ?', (name, password))
            return self.cursor.fetchone() is not None
    except ValueError:
        messagebox.showinfo("Erro","Erro na função de verificar se um usuário existe!")

    try:
        def close_connection(self):
            self.connection.close()
    except ValueError:
        messagebox.showinfo("Erro","Erro na função de fechar a conexão com o banco de usuários!")
