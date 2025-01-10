import tkinter as tk
import database

class Interface_Criar_Itens:
    def __init__(self):
        self.janela = tk.Tk()

    def Interface_Criar_Itens(self):

        def Botao_Salvar():
            string = f"Nome = {self.nome.get()},Quantidade = {self.quantidade.get()},Complemento = {self.complemento.get()}"
            db = database.Database("database.db")
            db.add_string(string)
            

        #configuracoes basicas
        self.janela.geometry("400x500")
        self.janela.title("")

        #imagens
        self.imagem = tk.PhotoImage(file="D:\Projetos de Programacao\Python\Lista_de_Compras\Imagens\interface_criar_item.png")
        self.imagem_label = tk.Label(self.janela,image=self.imagem)
        self.imagem_label.place(x=0,y=0,relheight=1,relwidth=1)

        #campo nome
        self.nome = tk.Entry(self.janela,font=(30),relief='flat')
        self.nome.place(x=204,y=90,height=50,width=170)

        #campo quantidade
        self.quantidade = tk.Entry(self.janela,font=(30),relief='flat')
        self.quantidade.place(x=204,y=207,height=50,width=170)

        #campo complemento
        self.complemento = tk.Entry(self.janela,font=(30),relief='flat')
        self.complemento.place(x=215,y=318,height=50,width=170)

        #botao salvar
        self.botao_salvar = tk.Button(self.janela,text="Salvar",font=30,background="white",relief='flat',command=Botao_Salvar)
        self.botao_salvar.place(x=115,y=422,height=58,width=170)

        self.janela.mainloop()

