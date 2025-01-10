import tkinter as tk
import interface_criar_itens
import interface_ver_itens


class Interface_Inicial:
    def __init__(self):
        self.janela = tk.Tk()

    def Interface_Inicial(self):

        def Botao_Ver_Itens():
            self.janela.destroy()
            ivi = interface_ver_itens.InterfaceVerItens()
            ivi.criar_interface()
            objeto_interface = Interface_Inicial()
            objeto_interface.Interface_Inicial()
            

        def Botao_Criar_Itens():
            self.janela.destroy()
            ici = interface_criar_itens.Interface_Criar_Itens()
            ici.Interface_Criar_Itens()
            objeto_interface = Interface_Inicial()
            objeto_interface.Interface_Inicial()

        #configuracoes basicas
        self.janela.geometry("400x500")
        self.janela.title("")

        #imagens
        self.imagem = tk.PhotoImage(file="D:\Projetos de Programacao\Python\Lista_de_Compras\Imagens\imagem_interface_inicial.png")
        self.imagem_label = tk.Label(self.janela,image=self.imagem)
        self.imagem_label.place(x=0,y=0,relheight=1,relwidth=1)

        #botao criar item
        self.botao_criar_item = tk.Button(self.janela,relief='flat',background="white",text="Criar Item",font=40,command=Botao_Criar_Itens)
        self.botao_criar_item.place(x=70,y=130,width=260,height=60)

        #botao ver itens salvos
        self.botao_ver_itens_salvos = tk.Button(self.janela,relief='flat',background="white",text="Ver Itens Salvos",font=40,command=Botao_Ver_Itens)
        self.botao_ver_itens_salvos.place(x=70,y=310,width=260,height=60)


        self.janela.mainloop()

janela = Interface_Inicial()
janela.Interface_Inicial()