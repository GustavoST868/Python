#librariies used
import sqlite3
from tkinter import messagebox

#class to create and manage the user database
class UserDatabase:
    def __init__(self, db_name='user_database.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_table()

    #function to connect to the user database
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            messagebox.showinfo("Info", f"Erro ao conectar ao banco {self.db_name}:\n{e}")

    #function to disconnect to the user database
    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
        except sqlite3.Error as e:
            messagebox.showinfo("Info", f"Erro ao desconectar do banco {self.db_name}:\n{e}")

    #function to create the data table
    def create_table(self, table_name='database_user'):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, name TEXT, password TEXT, email TEXT)"
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            messagebox.showinfo("Info", f"Erro na função de criar a tabela do {self.db_name}:\n{e}")

    #function to insert user data into the table
    def insert_user(self, table_name, name, password, email):
        try:
            query = f"INSERT INTO {table_name} (name, password, email) VALUES (?, ?, ?)"
            self.cursor.execute(query, (name, password, email))
            self.connection.commit()
        except sqlite3.Error as e:
            messagebox.showinfo("Info", f"Erro na função de inserir o usuário no {self.db_name}:\n{e}")

    #function to check if the user exists in the bank
    def authenticate_user(self, table_name, name, password):
        try:
            query = f"SELECT * FROM {table_name} WHERE name=? AND password=?"
            self.cursor.execute(query, (name, password))
            user = self.cursor.fetchone()
            return user is not None
        except sqlite3.Error as e:
            messagebox.showinfo("Info", f"Erro na função de autenticar o usuário no {self.db_name}:\n{e}")



