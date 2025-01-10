import tkinter as tk
import interfaceRegister 
import interfaceEnter
from tkinter import messagebox

class IntialInterface:
    def __init__(self):
        self.window = tk.Tk()

    def Window(self):
        
        try:
            def button_register():
                self.window.destroy()
                interface_register = interfaceRegister.RegisterInterface()
                interface_register.Window()
        except ValueError:
            messagebox("Erro","Erro na função do botão registrar!")


        try:
            def button_enter():
                self.window.destroy()
                enter_interface = interfaceEnter.EnterInterface()
                enter_interface.Window()
        except ValueError:
            messagebox("Erro","Erro na função do botão entrar!")

        self.window.title("")
        self.window.configure(background="#C7BEBE")

        self.label = tk.Label(self.window, text="Bem vindo a Loja", font=20)
        self.label.configure(background="#C7BEBE")
        self.label.place(x=150, y=100)

        self.button_enter = tk.Button(self.window, text="Entrar", relief='flat',command=button_enter)
        self.button_enter.configure(background="#A89E9E", width=15, height=5)
        self.button_enter.place(x=50, y=300)

        self.button_register = tk.Button(self.window, text="Registrar", relief='flat',command=button_register)
        self.button_register.configure(background="#A89E9E", width=15, height=5)
        self.button_register.place(x=225, y=300)

        self.window.geometry("400x500")
        self.window.mainloop()

if __name__ == "__main__":
    interface_initial = IntialInterface()
    interface_initial.Window()
