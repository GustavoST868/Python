import sqlite3

def create_table():
    conectar = sqlite3.connect('strings.db')
    c = conectar.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS strings
                 (string_id INTEGER PRIMARY KEY, content TEXT)''')
    conectar.commit()
    conectar.close()

def add_string(string):
    conectar = sqlite3.connect('strings.db')
    c = conectar.cursor()
    c.execute("INSERT INTO strings (content) VALUES (?)", (string,))
    conectar.commit()
    conectar.close()

def Criar_String():
    try:
        # Connect to the SQLite database
        conectar = sqlite3.connect('strings.db')
        
        # Create a cursor object
        cur = conectar.cursor()
        
        # Execute the SQL query
        cur.execute("SELECT * FROM strings")
        
        # Fetch all the rows from the database
        rows = cur.fetchall()
        
        # Create a list to store the string representation of each row
        resultado = []
        
        # Iterate over each row
        for row in rows:
            # Convert each row to a string and append it to the result list
            resultado.append(str(row))
        
        # Return the string representation of all the rows
        return "\n".join(resultado)
    
    except sqlite3.Error as error:
        print("Error occurred while fetching data:", error)
    
    finally:
        # Close the database connection
        if conectar:
            conectar.close()

# Função para deletar uma string do banco de dados
def Deletar_Dado(string):
    try:
        # Conectar ao banco de dados SQLite
        conectar = sqlite3.connect('strings.db')
        
        # Criar um objeto de cursor
        cur = conectar.cursor()
        
        # Executar a consulta SQL para deletar a string
        cur.execute("DELETE FROM strings WHERE content=?", (string,))
        
        # Commit para salvar as alterações no banco de dados
        conectar.commit()
        print(f'String "{string}" deletada com sucesso do banco de dados.')
    
    except sqlite3.Error as error:
        print("Erro ao deletar a string:", error)
    
    finally:
        # Fechar a conexão com o banco de dados
        if conectar:
            conectar.close()


create_table()

def Format(string):
    data = []  
    i = 0
    while i < len(string):
        if string[i] == '{' or string[i] == '[':
            i += 1
            while string[i] != '}' or string[i] == ']':
                data.append(string[i])
                i += 1
            data.append("\n")  
        else:
            data.append(string[i])
        i += 1
    data_format = ''.join(data)
    return data_format

Format("{gustavo} {Gabriel} {Tiago}")

def Database_String():
    data = Criar_String()
    data_2 = Format(data)
    return data_2

