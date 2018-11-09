from janela_principal import Janela_Principal
from bd_simulado import  BD_simulado

#Criando uma classe de controle:
class Controle():
    #Método construtor:
    def __init__(self):
        #Atributos:
        self.bd = BD_simulado()
        self.jnl = Janela_Principal(self)
        self.jnl.mainloop()

    #Método para retornar a lista de compras:
    def get_lista_compra(self):
        return self.bd.get_lista_compra()