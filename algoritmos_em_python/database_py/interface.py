import tkinter as tk
import database
import entrada_de_dados

class Interface:

    def __init__(self):
        self.janela = tk.Tk()

    def interface(self):
        db = database.Database()

        def Botao_Apagar_Dados():
            Botao_Apagar()
            string = str(self.campo_Dado_Apagar.get())
            db.Deletar(string)
            Botao_Mostrar_Dados()

        def Botao_Dado():
            string = str(self.campo_Dado.get())
            db.Inserir(string)
            Botao_Apagar()
            Botao_Mostrar_Dados()

        def Botao_Mostrar_Dados():
            self.texto.insert("1.0", db.Mostrar())

        def Botao_Apagar():
            self.texto.delete("1.0", tk.END) 

        def Botao_Ordenar_Alfabeticamente():
            Botao_Apagar()
            db.Ordenar_Alfabeto()
            Botao_Mostrar_Dados()

        self.janela.title("Banco de Dados Local")
        self.janela.geometry("600x400")

        self.botao_mostrar_texto = tk.Button(self.janela, text="    Mostrar Dados      ", command=Botao_Mostrar_Dados)
        self.botao_mostrar_texto.place(x=0, y=0)

        self.botao_apagar = tk.Button(self.janela, text="             Apagar             ", command=Botao_Apagar)
        self.botao_apagar.place(y=0, x=90+30)

        self.botao_Ordenar = tk.Button(self.janela,text="  Ordenar Alfabeticamente  ",command=Botao_Ordenar_Alfabeticamente)
        self.botao_Ordenar.place(x=140+40+70,y=0)

        self.label_Adicionar = tk.Label(self.janela,text="Adicionar dado:")
        self.label_Adicionar.place(x=300+80+30,y=0)

        self.label_Apagar = tk.Label(self.janela,text="Apagar dado:")
        self.label_Apagar.place(x=300+80+30,y=100)

        self.label_Dado = tk.Label(self.janela,text="Dado:")
        self.label_Dado.place(x=300+80+30,y=30)

        self.label_Dado = tk.Label(self.janela,text="Dado:")
        self.label_Dado.place(x=300+80+30,y=130)

        self.campo_Dado = tk.Entry(self.janela)
        self.campo_Dado.place(x=350+80+30,y=30)

        self.campo_Dado_Apagar = tk.Entry(self.janela)
        self.campo_Dado_Apagar.place(x=350+80+30,y=130)

        self.botao_Dado = tk.Button(self.janela,text="Adicionar",command=Botao_Dado)
        self.botao_Dado.place(x=300+80+30,y=60)

        self.botao_Dado_Apagar = tk.Button(self.janela,text="Apagar",command=Botao_Apagar_Dados)
        self.botao_Dado_Apagar.place(x=300+80+30,y=160)

        self.texto = tk.Text(self.janela)
        self.texto.place(x=0, y=29, width=297+80+30, height=500)
        self.janela.mainloop()

if __name__ == "__main__":
    janela = Interface()
    janela.interface()
