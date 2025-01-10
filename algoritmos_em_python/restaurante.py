######################################################################################################################
###########################___INTERFACE___############################################################################
######################################################################################################################

# used libraries
import tkinter as tk




def Student_Window():
    student_window = tk.Tk()
    student_window.geometry("400x400")
    student_window.configure(background="gray")
    label = tk.Label(student_window, text=global_text, padx=0, pady=0)
    label.pack(side="top")
    student_window.title("")
    student_window.mainloop()


def Initial():
    def cliente_click():
        root.destroy()
        Student_Window()

    def funcionario_click():
        root.destroy()
        LoginWindowOfficial()

    root = tk.Tk()
    root.geometry("150x100")
    root.configure(background="gray")
    root.title("Janela com Botões")

    botao_cliente = tk.Button(root, text="Cliente", command=cliente_click)
    botao_funcionario = tk.Button(root, text="Funcionário", command=funcionario_click)

    botao_cliente.pack(side=tk.LEFT, padx=8, pady=8)
    botao_funcionario.pack(side=tk.LEFT, padx=8, pady=8)
    root.mainloop()


def LoginWindowOfficial():
    # function for official login window
    def VerifyOfficial():
        official_user = official_user_field.get()
        official_password = official_password_field.get()
        if official_user == "" and official_password == "":
            official_window.destroy()
            WindowOfficial()
        else:
            print("Funcionário não correspondente!")

    def Back():
        official_window.destroy()
        Initial()

    # window settings for official login
    official_window = tk.Tk()
    official_window.title("")
    official_window.geometry("200x100")
    official_window.configure(background="gray")

    # official user label field and padding
    label_official_user = tk.Label(official_window, text="Usuário:")
    label_official_user.grid(row=0, column=0, padx=5, pady=5)

    # official user text field and padding
    official_user_field = tk.Entry(official_window)
    official_user_field.grid(row=0, column=1, padx=5, pady=5)

    # official password label field and padding
    label_official_password = tk.Label(official_window, text=" Senha: ")
    label_official_password.grid(row=1, column=0, padx=5, pady=5)

    # official password text field and padding
    official_password_field = tk.Entry(official_window, show="*")
    official_password_field.grid(row=1, column=1, padx=5, pady=5)

    # button and padding
    button_entrar_official = tk.Button(
        official_window, text="Entrar", command=VerifyOfficial
    )

    button_entrar_official.grid(row=2, column=0, pady=2, padx=2)

    button_go_to_back = tk.Button(official_window, text="Voltar", command=Back)
    button_go_to_back.grid(row=2, column=1, padx=2, pady=2)

    # keep the page visible
    official_window.mainloop()


def WindowOfficial():
    def SaveInDataBase():
        data_text = f"Dia da semana = {day_week_field.get()}\nSuco          = {juice_fild.get()}\nProteina      = {protein_fild.get()}\nCarboidratos  = {carbohydrates_fild.get()}\nSalada        = {salad_fild.get()}\n"
        return data_text
        

    def Go_to_Back():
        window_official.destroy()
        LoginWindowOfficial()

    # window official settings
    window_official = tk.Tk()
    window_official.title("Cardápio")
    window_official.configure(background="gray")
    window_official.geometry("220x155")

    # day of the week label
    label_day_week = tk.Label(window_official, text="Dia da semana:")
    label_day_week.configure(background="lightgray")
    label_day_week.grid(row=0, column=0, padx=2, pady=2)

    # day of the week field
    day_week_field = tk.Entry(window_official)
    day_week_field.grid(row=0, column=1, padx=2, pady=2)

    # juice label
    juice_label = tk.Label(window_official, text="        Suco:        ")
    juice_label.configure(background="lightgray")
    juice_label.grid(row=1, column=0, padx=2, pady=2)

    # juice fild
    juice_fild = tk.Entry(window_official)
    juice_fild.grid(row=1, column=1, padx=2, pady=2)

    # protein label
    protein_label = tk.Label(window_official, text="     Proteina:     ")
    protein_label.configure(background="lightgray")
    protein_label.grid(row=2, column=0, padx=2, pady=2)

    # protein fild
    protein_fild = tk.Entry(window_official)
    protein_fild.grid(row=2, column=1, padx=2, pady=2)

    # carbohydrates label
    carbohydrates_label = tk.Label(window_official, text=" Carboidratos: ")
    carbohydrates_label.configure(background="lightgray")
    carbohydrates_label.grid(row=3, column=0, padx=2, pady=2)

    # carbohydrates fild
    carbohydrates_fild = tk.Entry(window_official)
    carbohydrates_fild.grid(row=3, column=1, padx=2, pady=2)

    # salad label
    salad_label = tk.Label(window_official, text="        Salada:      ")
    salad_label.configure(background="lightgray")
    salad_label.grid(row=4, column=0, padx=2, pady=2)

    # salad fild
    salad_fild = tk.Entry(window_official)
    salad_fild.grid(row=4, column=1, padx=2, pady=2)

    # button to go back
    button_back = tk.Button(window_official, text="Voltar", command=Go_to_Back)
    button_back.grid(row=5, column=0, padx=2, pady=2)

    # save button
    button_save = tk.Button(window_official, text="Salvar",command=SaveInDataBase)
    button_save.grid(row=5, column=1, padx=2, pady=2)

    window_official.mainloop()


####################################################################################################################
###########################___DATABASE___############################################################################
####################################################################################################################

# list to store the values
data_base = []

# insert value into the database
def Push(data):
    data_base.append(str(data))


# print the current state of the database
def PrintDataBase():
    data_base_text = f"\nDataBase:\n{data_base}"
    return data_base_text


# remove a specific value from the database
def RemoveData(data):
    data_base.remove(str(data))


# clear the entire database
def ClearDatabase():
    data_base.clear()


# search for data in the banck
def Search(data):
    result = False
    for data in data_base:
        if data == str(data):
            result = True
            break
    if result:
        print("\nO dado existe no banco!")
    else:
        print("\nNão  existe no banco!")


####################################################################################################################
###########################___PROGRAM___############################################################################
####################################################################################################################

# calling the window
window = Initial()
