import tkinter as tk
import address
import intefaceProduct
from tkinter import messagebox

class GetAddress:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        try:
            def button_next():
                address_ = address.Address()
                address_.insert_address(self.entry_country.get(),self.entry_state.get(),self.entry_city.get(),self.entry_street.get(),self.entry_number.get(),self.entry_complement.get()) 
                self.window.destroy()
                interface_product = intefaceProduct.InterfaceProduct()
                interface_product.Window()
        except ValueError:
            messagebox("Erro","Erro na função do botão próximo!")
            
            

        self.window.configure(background="#C7BEBE")

        self.label_country = tk.Label(self.window, text="Pais")
        self.label_country.configure(background="#C7BEBE")
        self.label_country.grid(row=0, column=0, padx=10, pady=10)

        self.label_state = tk.Label(self.window, text="Estado")
        self.label_state.configure(background="#C7BEBE")
        self.label_state.grid(row=1, column=0, padx=10, pady=10)

        self.label_city = tk.Label(self.window, text="Cidade")
        self.label_city.configure(background="#C7BEBE")
        self.label_city.grid(row=2, column=0, padx=10, pady=10)

        self.label_street = tk.Label(self.window, text="Rua")
        self.label_street.configure(background="#C7BEBE")
        self.label_street.grid(row=3, column=0, padx=10, pady=10)

        self.label_number = tk.Label(self.window, text="Número")
        self.label_number.configure(background="#C7BEBE")
        self.label_number.grid(row=4, column=0, padx=10, pady=10)

        self.label_cep = tk.Label(self.window, text="CEP")
        self.label_cep.configure(background="#C7BEBE")
        self.label_cep.grid(row=5, column=0, padx=10, pady=10)

        self.label_complement = tk.Label(self.window, text="Complemento")
        self.label_complement.configure(background="#C7BEBE")
        self.label_complement.grid(row=6, column=0, padx=10, pady=10)

        self.entry_country = tk.Entry(self.window)
        self.entry_country.configure(background="#DAD6D6")
        self.entry_country.grid(row=0, column=1, padx=10, pady=10)

        self.entry_state = tk.Entry(self.window)
        self.entry_state.configure(background="#DAD6D6")
        self.entry_state.grid(row=1, column=1, padx=10, pady=10)

        self.entry_city = tk.Entry(self.window)
        self.entry_city.configure(background="#DAD6D6")
        self.entry_city.grid(row=2, column=1, padx=10, pady=10)

        self.entry_street = tk.Entry(self.window)
        self.entry_street.configure(background="#DAD6D6")
        self.entry_street.grid(row=3, column=1, padx=10, pady=10)

        self.entry_number = tk.Entry(self.window)
        self.entry_number.configure(background="#DAD6D6")
        self.entry_number.grid(row=4, column=1, padx=10, pady=10)

        self.entry_cep = tk.Entry(self.window)
        self.entry_cep.configure(background="#DAD6D6")
        self.entry_cep.grid(row=5, column=1, padx=10, pady=10)

        self.entry_complement = tk.Entry(self.window)
        self.entry_complement.configure(background="#DAD6D6")
        self.entry_complement.grid(row=6, column=1, padx=10, pady=10)

        self.button_next = tk.Button(self.window, text="Próximo",command=button_next)
        self.button_next.configure(background="#A89E9E")
        self.button_next.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.window.title("")
        self.window.mainloop()

    
