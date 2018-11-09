#Classe Item_Compra
class Item_Compra():
    #Método Construtor:
    def __init__(self, nome, qtde):
        #Atributos:
        self.nome = nome
        self.qtde = qtde

    #Método que converte a classe em texto:
    def to_string(self):
        return self.nome + ';' +str(self.qtde)

    #Método para retornar o nome:
    def get_nome(self):
        return self.nome
    #Método para retornar a qtde:
    def get_qtde(self):
        return self.qtde