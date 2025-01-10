class Database:
    def __init__(self):
        self.chave_primaria = []
        self.dado = []
        self.ordenar = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]

    def Inserir(self, dado):
        chave = len(self.chave_primaria) + 1
        self.chave_primaria.append(chave)
        self.dado.append(dado)
    
    def Deletar(self,dado):
        indece = self.dado.index(dado)
        self.dado.pop(indece)

    def Ordenar_Alfabeto(self):
        auxiliar = []
        for letra in self.ordenar:
            for dado in self.dado:
                if dado[0] == letra:
                    auxiliar.append(dado)
        self.dado.clear()
        self.dado.extend(auxiliar)

    def Mostrar(self):
        conjunto_de_dados = []
        conjunto_de_dados.append("BANCO DE DADOS :\n")
        for chave, dado in zip(self.chave_primaria, self.dado):
            conjunto_de_dados.append(f"Nome:[ {dado} ] , Indice:[ {chave} ]")
        separador = "\n"
        conjunto_de_dados.append("\n\n\n")
        return separador.join(conjunto_de_dados)



