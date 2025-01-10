import tkinter as tk

class Interface:
    #construtor
    def __init__(self):
        self.window = tk.Tk()
        self.photo = tk.PhotoImage(file="D:\Projetos-de-Programacao\Python\Interfaces\imagem.png")
        self.label = tk.Label(self.window, image=self.photo)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

    def Interface_Principal(self):
        #configurações básicas
        self.window.title("")
        self.window.geometry("400x400")
        self.window.configure(background="gray")

        self.campo_senha = tk.Entry(self.window)
        self.campo_senha.place(x=170+20, y=220)

        self.campo_usuario = tk.Entry(self.window)
        self.campo_usuario.place(x=170+20, y=158)

        self.botao_entrar = tk.Button(self.window,text="Entrar",width=15,height=2)
        self.botao_entrar.place(x=150,y=300)
        self.botao_entrar.configure(background="RoyalBlue1")

        self.window.mainloop()

janela = Interface()
janela.Interface_Principal()