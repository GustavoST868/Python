# Structures for storing values
name = []
value = []

# Function to insert product into the list
def Insert_Product(name_product, value_product):
    name.append(name_product)
    value.append(value_product)
    
# Function to print product data,return the database in a single string
def Print_Database():
    string = []
    separator = "\n"
    for i in range(len(name)):
        string.append(f"Nome = {name[i]}  Valor = {value[i]} Índice = {i}")
    return separator.join(string)

#function to remove product 
def Remove_Product(index):
    if 0 <= index < len(name):
        name.pop(index)
        value.pop(index)    

def Get_value(indece):
    value_database = float(value[indece])
    return value_database
