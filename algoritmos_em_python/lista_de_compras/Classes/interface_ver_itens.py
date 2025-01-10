import tkinter as tk
import database  # Certifique-se de que você tem um arquivo database.py no mesmo diretório ou ajuste o caminho conforme necessário.

class InterfaceVerItens:
    def __init__(self):
        self.janela = tk.Tk()

    def criar_interface(self):
        # Configurações básicas
        self.janela.geometry("400x500")
        self.janela.title("")

        # Imagens
        self.imagem = tk.PhotoImage(file="D:\\Projetos de Programacao\\Python\\Lista_de_Compras\\Imagens\\interface_ver_itens.png")
        self.imagem_label = tk.Label(self.janela, image=self.imagem)
        self.imagem_label.place(x=0, y=0, relheight=1, relwidth=1)

        self.campo = tk.Text(self.janela)
        self.campo.place(x=10, y=10, width=380, height=430)

        db = database.Database('database.db')  # Certifique-se de que o arquivo do banco de dados está no mesmo diretório ou ajuste o caminho.
        strings = db.get_all_strings()
        for string in strings:
            self.campo.insert(tk.END, string)

        self.janela.mainloop()


