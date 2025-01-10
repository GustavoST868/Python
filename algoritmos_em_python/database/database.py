from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Conectar ao banco de dados SQLite (ou criar um novo se não existir)
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Criar a tabela de usuários (se não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade TEXT
    )
''')

conexao.commit()
conexao.close()

# Função para adicionar um novo usuário ao banco de dados
def adicionar_usuario(nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    conexao.commit()
    conexao.close()

# Adicionar usuários ao banco (em forma de strings)
adicionar_usuario("Gustavo", None)
adicionar_usuario("Tiago", "10")

# Função para obter todos os usuários em forma de strings
def obter_usuarios_como_strings():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conexao.close()
    usuarios_strings = []
    for usuario in usuarios:
        usuario_string = f'ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2] or "N/A"}'
        usuarios_strings.append(usuario_string)
    return usuarios_strings

# Endpoint para obter todos os usuários em forma de strings
@app.route('/usuarios', methods=['GET'])
def obter_usuarios_endpoint():
    usuarios_strings = obter_usuarios_como_strings()
    return jsonify({'usuarios': usuarios_strings})

# Endpoint para adicionar um novo usuário
@app.route('/usuarios', methods=['POST'])
def adicionar_usuario_endpoint():
    dados_usuario = request.get_json()
    nome = dados_usuario.get('nome')
    idade = dados_usuario.get('idade')
    
    # Se a idade for None, defina como string vazia ("")
    idade = idade or ""
    
    if nome is None:
        return jsonify({'erro': 'Nome é obrigatório'}), 400
    
    adicionar_usuario(nome, idade)
    return jsonify({'mensagem': 'Usuário adicionado com sucesso!'})



def obter_usuarios_formatados():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conexao.close()
    usuarios_formatados = []
    for usuario in usuarios:
        usuario_formatado = f'ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2] or "N/A"}\n'
        usuarios_formatados.append(usuario_formatado)
    return '\n'.join(usuarios_formatados)

if __name__ == '__main__':
    app.run(debug=True)
