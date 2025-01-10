import tkinter as tk
import interfaceIntial as interfaceIntial 
import interfaceGetAddress as interfaceGetAddress 
import user 
from tkinter import messagebox


class RegisterInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        try:
            def button_back():
                self.window.destroy()

                interface_initial = interfaceIntial.IntialInterface()
                interface_initial.Window()
        except ValueError:
            messagebox("Erro","Erro na função do botão voltar!")

        try:
            def button_next():
                name = self.entry_name.get()
                password = self.entry_password.get()
                user_ = user.User()
                user_.insert_user(name,password,False)
                self.window.destroy()
                get_address = interfaceGetAddress.GetAddress()
                get_address.Window()
        except ValueError:
            messagebox("Erro","Erro na função do botão próximo!")

        self.window.configure(background="#C7BEBE")
        self.window.title("")

        self.label_name = tk.Label(self.window, text="Nome")
        self.label_name.configure(background="#C7BEBE")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.configure(background="#DAD6D6")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(self.window, text="Senha")
        self.label_password.configure(background="#C7BEBE")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.configure(background="#DAD6D6")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_back = tk.Button(self.window, text="Voltar", command=button_back, relief='flat')
        self.button_back.configure(background="#A89E9E")
        self.button_back.grid(row=2, column=0, padx=10, pady=10)

        self.button_next = tk.Button(self.window, text="Próximo", relief='flat', command=button_next)
        self.button_next.configure(background="#A89E9E")
        self.button_next.grid(row=2, column=1, padx=10, pady=10)

        self.window.mainloop()


