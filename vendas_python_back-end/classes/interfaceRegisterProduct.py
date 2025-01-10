import tkinter as tk
import intefaceProduct
from tkinter import messagebox
import product
class InteraceRegisterProduct:
    def __init__(self):
        self.window = tk.Tk()


    def Window(self):

        try:
            def button_back():
                self.window.destroy()
                interface_product = intefaceProduct.InterfaceProduct()
                interface_product.Window()
        except ValueError:
            messagebox.showinfo("Erro","Erro  na função do botão voltar!")

        try:
            def button_register():
                product_ = product.Product()
                product_.insert_product(self.entry_name.get(),self.entry_price.get(),self.entry_size.get(),self.entry_description.get())
                messagebox.showinfo.showinfo("Informação","Produto salvo no banco!")
        except ValueError:
            messagebox.showinfo("Erro","Erro  na função do botão voltar!")


        self.window.configure(background="#C7BEBE")

        self.label_name = tk.Label(self.window,text="Nome")
        self.label_name.configure(background="#C7BEBE")
        self.label_name.grid(row=0,column=0,padx=5,pady=5)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.configure(background="#DAD6D6")
        self.entry_name.grid(row=0,column=1,padx=5,pady=5)

        self.label_price = tk.Label(self.window,text="Preço")
        self.label_price.configure(background="#C7BEBE")
        self.label_price.grid(row=1,column=0,padx=5,pady=5)

        self.entry_price = tk.Entry(self.window)
        self.entry_price.configure(background="#DAD6D6")
        self.entry_price.grid(row=1,column=1,padx=5,pady=5)

        self.label_size = tk.Label(self.window,text="Tamanho")
        self.label_size.configure(background="#C7BEBE")
        self.label_size.grid(row=2,column=0,padx=5,pady=5)

        self.entry_size = tk.Entry(self.window)
        self.entry_size.configure(background="#DAD6D6")
        self.entry_size.grid(row=2,column=1)

        self.label_description = tk.Label(self.window,text="Descrição")
        self.label_description.configure(background="#C7BEBE")
        self.label_description.grid(row=3,column=0,padx=5,pady=5)

        self.entry_description = tk.Entry(self.window)
        self.entry_description.configure(background="#DAD6D6")
        self.entry_description.grid(row=3,column=1)

        self.button_back = tk.Button(self.window,text="Voltar",command=button_back)
        self.button_back.configure(background="#A89E9E")
        self.button_back.grid(row=4,column=0,padx=5,pady=5)

        self.button_next = tk.Button(self.window,text="Registrar",command=button_register)
        self.button_next.configure(background="#A89E9E")
        self.button_next.grid(row=4,column=1,padx=5,pady=5)


        self.window.title("")
        self.window.mainloop()

