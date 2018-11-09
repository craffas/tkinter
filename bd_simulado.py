from item_compras import Item_Compra

#Classe BD_Simulado:
class BD_simulado():
    #Método Construtor:
    def __init__(self):
        #Atributos:
        self.lista_compra = []
        self.carregar_lista_compra()

    #Método carregar lista de compra
    def carregar_lista_compra(self):
        #Colocar aqui o código para abrir arquivo.
        # Abrindo o arquivo txt:
        #Cada linha do arquivo separar nome e quantidade split(;)
        #Cada linha do arquivo criar um objeto de item_compra
        #Inserir o objeto na lista de compra

        #Remover essa parte
        item1 = Item_Compra('tomate', 10)
        item2 = Item_Compra('banana', 5)
        item3 = Item_Compra('Café', 1)
        self.lista_compra.append(item1)
        self.lista_compra.append(item2)
        self.lista_compra.append(item3)
        #Remover até aqui.

    def gravar_lista_compra(self):
        #Abrir o arquivo para gravação (Apagar o conteúdo)
        #Percorrer a lista
        #Para cada item da lista, converter em string
        #Salvar no arquivo

        #Remover essa parte (Exemplo)
        for item in self.lista_compra:
            print(item.to_string())
        #Remover até aqui

    #Método para rerornar um Item_compra de acordo com o seu nome:
    def get_item_compra(self, nome):
        #Percorrer a lista:
        for item in self.lista_compra:
            if (item.get_nome()==nome):
                return item
        #Se não encontrar:
        return None

    #Método para retornar lista de compras:
    def get_lista_compra(self):
        return self.lista_compra