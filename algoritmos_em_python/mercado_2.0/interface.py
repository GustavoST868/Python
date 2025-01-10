import tkinter as tk
import database 

import tkinter as tk
import database

# Variáveis globais
Entry_indice = None
label_value = None

def Button_add():
    global Entry_indice, label_value
    global value_final
    
    try:
        indece = int(Entry_indice.get())
        value_database = database.Get_value(indece)
        value_final += value_database
        label_value.config(text=f"Valor => R${value_final}")
    except ValueError:
        label_value.config(text="Invalid input")

def Interface_Create_Lista():
    global Entry_indice, label_value
    global value_final

    value_final = 0  

    window5 = tk.Tk()
    window5.title("Inserir Produto")
    window5.configure(background="sky blue")
    window5.geometry("350x100")

    label_value = tk.Label(window5, text="Valor => R$00,00")
    label_value.configure(background="sky blue")
    label_value.grid(row=0, column=0, padx=5, pady=5)

    label_indice = tk.Label(window5, text="Índice:")
    label_indice.configure(background="sky blue")
    label_indice.grid(row=1, column=0, padx=5, pady=5)

    Entry_indice = tk.Entry(window5)
    Entry_indice.grid(row=1, column=1, padx=5, pady=5)

    button_add = tk.Button(window5, text="Adicionar", command=Button_add)
    button_add.configure(background="lime green")
    button_add.grid(row=2, column=0, padx=5, pady=5)

    window5.mainloop()


#interface to delete product
def Interface_Delete_Product():

    #delete button function
    def Button_delete():
        index = int(field_index.get())
        database.Remove_Product(index)
    
   # Create the window
    window4 = tk.Tk()
    window4.title("Deletar Produto")
    window4.configure(background="sky blue")
    window4.geometry("350x80")

    # label index
    label_index = tk.Label(window4,text="Indece:")
    label_index.configure(background="sky blue")
    label_index.grid(row=0,column=0,padx=5,pady=5)

    #field index
    field_index = tk.Entry(window4,width=39)
    field_index.configure(background="gray80")
    field_index.grid(row=0,column=1,padx=5,pady=5)

    #button delete
    button_delete = tk.Button(window4,text="Deletar",command=Button_delete)
    button_delete.configure(background="lime green")
    button_delete.grid(row=1,column=0,padx=5,pady=5)

    window4.mainloop()

#interface to show the dababase
def Interface_Print_Database():
    
    # Create the window
    window3 = tk.Tk()
    window3.title("Banco de dados")
    window3.configure(background="sky blue")
    window3.geometry("350x400")

    # Create a Scrollbar widget
    scrollbar = tk.Scrollbar(window3, orient=tk.VERTICAL)
    scrollbar.configure(background="sky blue")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Get the big string from the database
    large_string = database.Print_Database()

    # Create a Text widget inside the window with the associated scrollbar
    text = tk.Text(window3, wrap=tk.WORD, width=40, height=10, yscrollcommand=scrollbar.set)
    text.configure(background="sky blue")
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar.config(command=text.yview)

   # Insert the large string into the Text widget
    text.insert(tk.END, large_string)
    text.config(state=tk.DISABLED)


    window3.mainloop()

#Function to create the first interface.
def Interface_add_Product():
    
    #function to save data to the database
    def Function_Button_Save():
        name_product = field_name_product.get()
        value_product = field_value_product.get()
        database.Insert_Product(name_product,value_product)

   #window settings
    window2 = tk.Tk()
    window2.title("Mercado")
    window2.configure(background="sky blue")
    window2.geometry("359x100")

    #label for product name
    label_name_product = tk.Label(window2,text="Nome do produto :")
    label_name_product.configure(background="sky blue")
    label_name_product.grid(row=0,column=0,padx=5,pady=5)

    #label for product value
    label_value_product = tk.Label(window2,text="Valor do produto :")
    label_value_product.configure(background="sky blue")
    label_value_product.grid(row=2,column=0,padx=5,pady=5)

    #field for product name
    field_name_product = tk.Entry(window2,width=35)
    field_name_product.configure(background="gray80")
    field_name_product.grid(row=0,column=1,padx=5,pady=5)

    #field for product value
    field_value_product = tk.Entry(window2,width=35)
    field_value_product.configure(background="gray80")
    field_value_product.grid(row=2,column=1,padx=5,pady=5)

    #button to save
    button_save = tk.Button(window2,text="Salvar",command=Function_Button_Save)
    button_save.configure(background="lime green")
    button_save.grid(row=3,column=0,padx=5,pady=5)

    window2.mainloop()



#main interface
def First_Interface():
    #window settings
    window = tk.Tk()
    window.title("Mercado")
    window.configure(background="sky blue")
    window.geometry("350x389")

    #button create shopping list
    button = tk.Button(window,text="Criar lista de compras",width=47,height=5,command=Interface_Create_Lista)
    button.configure(background="deep sky blue")
    button.grid(row=0,column=0,padx=5,pady=5)

    #button show products from the database
    button = tk.Button(window,text="Mostrar produtos registrados",width=47,height=5,command=Interface_Print_Database)
    button.configure(background="deep sky blue")
    button.grid(row=1,column=0,padx=5,pady=5)

    #button to add product
    button = tk.Button(window,text="Adicionar produto",width=47,height=5,command=Interface_add_Product)
    button.configure(background="deep sky blue")
    button.grid(row=2,column=0,padx=5,pady=5)

    #button to delete product
    button = tk.Button(window,text="Excluir produto",width=47,height=5,command=Interface_Delete_Product)
    button.configure(background="deep sky blue")
    button.grid(row=3,column=0,padx=5,pady=5)

    window.mainloop()
