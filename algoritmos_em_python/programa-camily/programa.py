import tkinter as tk
from tkinter import messagebox
import os
import sqlite3

import sqlite3

class BancoDeDados:
    def __init__(self, nome_do_banco):
        self.conexao = sqlite3.connect(nome_do_banco)
        self.cursor = self.conexao.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS frases (frase TEXT);")

    def add_frase(self, frase):
        self.cursor.execute("INSERT INTO frases (frase) VALUES (?);", (frase,))
        self.conexao.commit()

    def get_frases(self):
        self.cursor.execute("SELECT frase FROM frases;")
        frases = self.cursor.fetchall()
        return "\n".join(frase[0] for frase in frases)

    def delete_all_data(self):
        self.cursor.execute("DELETE FROM frases;")
        self.conexao.commit()

if __name__ == "__main__":
    banco = BancoDeDados("frases.db")


def Interface_Escrever():

    def Botao_Registrar():
        db = BancoDeDados("frases.db")
        string = campo_escrever.get("1.0", "end-1c")
        db.add_frase(string)
        print(db.get_frases())
        
    janela = tk.Tk()
    janela.title("")
    janela.geometry("600x600")

    # Caminho relativo para a imagem menu_opcoes.png
    caminho_menu_opcoes = os.path.join(os.path.dirname(__file__), "image_botao_salvar.png")
    imagem2 = tk.PhotoImage(file=caminho_menu_opcoes)
    imagem_label2 = tk.Label(janela, image=imagem2)
    imagem_label2.place(x=0, y=0, relheight=1, relwidth=1)

    campo_escrever = tk.Text(janela,bg='lightpink')
    campo_escrever.place(x=10,y=40,width=570,height=470)

    botao_registrar = tk.Button(janela,text="Registrar",relief='flat',font=20,command=Botao_Registrar)
    botao_registrar.place(x=230,y=540,width=140,height=40)

    janela.mainloop()


def Interface_Registros():
    janela = tk.Tk()
    janela.title("")
    janela.geometry("600x600")

    caminho_registros = os.path.join(os.path.dirname(__file__), "registro_imagem.png")
    imagem2 = tk.PhotoImage(file=caminho_registros)
    imagem_label2 = tk.Label(janela, image=imagem2)
    imagem_label2.place(x=0, y=0, relheight=1, relwidth=1)

    bd = BancoDeDados("frases.db")
    texto = bd.get_frases()
    campo_registros = tk.Text(janela,bg='lightpink')
    campo_registros.place(x=10,y=40,width=570,height=470)
    campo_registros.insert(tk.END, texto)
    
    janela.mainloop()


def Interface_Menu_Opcoes():
    def Salvos():
        janela.destroy()
        Interface_Registros()
        Interface_Menu_Opcoes()

    def Botao_escrever():
        janela.destroy()
        Interface_Escrever()
        Interface_Menu_Opcoes()

    janela = tk.Tk()
    janela.title("")
    janela.geometry("600x600")

    # Caminho relativo para a imagem menu_opcoes.png
    caminho_menu_opcoes = os.path.join(os.path.dirname(__file__), "menu_opcoes.png")
    imagem2 = tk.PhotoImage(file=caminho_menu_opcoes)
    imagem_label2 = tk.Label(janela, image=imagem2)
    imagem_label2.place(x=0, y=0, relheight=1, relwidth=1)

    botao_escrever = tk.Button(janela, relief='flat', background="white", text="Escrever", font=("Helvetica", 25),command=Botao_escrever)
    botao_escrever.place(x=100, y=200, width=400, height=90)

    botao_textos_salvos = tk.Button(janela, relief='flat', background="white", text="Textos Registrados", font=("Helvetica", 25),command=Salvos)
    botao_textos_salvos.place(x=110, y=377, width=400, height=89)

    janela.mainloop()

def Interface_Login():
    def Botao_Entrar():
        if campo_usuario.get() == "Camily" and campo_senha.get() == "gustavo":
            janela.destroy()
            Interface_Menu_Opcoes()
        else:
            messagebox.showerror("Erro", "Senha incorreta. Tente novamente.")

    janela = tk.Tk()
    janela.title("")
    janela.geometry("400x600")

    # Caminho relativo para a imagem imagem.png
    caminho_imagem = os.path.join(os.path.dirname(__file__), "imagem.png")
    imagem = tk.PhotoImage(file=caminho_imagem)
    imagem_label = tk.Label(janela, image=imagem)
    imagem_label.place(x=0, y=0, relheight=1, relwidth=1)

    campo_usuario = tk.Entry(janela, relief='flat', fg='red', font=15)
    campo_usuario.place(x=165, y=242, width=178, height=40)

    campo_senha = tk.Entry(janela, relief='flat', fg='red', show='*', font=15)
    campo_senha.place(x=165, y=360, width=178, height=40)

    botao_entrar = tk.Button(janela, text="Entrar", fg='red', relief='flat', command=Botao_Entrar)
    botao_entrar.place(x=112, y=480, width=178, height=40)

    janela.mainloop()

if __name__ == "__main__":
    banco = BancoDeDados("frases.db")
    Interface_Login()