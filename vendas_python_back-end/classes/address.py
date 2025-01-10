import sqlite3
from tkinter import messagebox

class Address:
    def __init__(self):
        self.connection = sqlite3.connect('addresses.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS addresses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country TEXT NOT NULL,
                state TEXT NOT NULL,
                city TEXT NOT NULL,
                street TEXT NOT NULL,
                number INTEGER NOT NULL,
                complement TEXT
            )
        ''')
        self.connection.commit()

    try:
        def insert_address(self, country, state, city, street, number, complement):
            self.cursor.execute('''
                INSERT INTO addresses (country, state, city, street, number, complement)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (country, state, city, street, number, complement))
            self.connection.commit()
    except ValueError:
        messagebox.showinfo("Erro","Erro na função de inserir endereço!")


    try:
        def close_connection(self):
            self.connection.close()
    except ValueError:
        messagebox.showinfo("Erro","Erro na função de fechar a conexão com o banco de endereços!")
