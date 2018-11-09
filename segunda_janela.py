#Importação de bibliotecas:
from tkinter import *
from tkinter import messagebox

#Classe Segunda_Janela
class Segunda_Janela(Toplevel):
    #Método Construtor:
    def __init__(self, parent):
        #Chamar o init da classe mãe:
        super().__init__(parent)
        # Ajustar tamanho
        self.geometry('380x440+50+100')
        #Definindo cor de fundo da tela:
        corFundo = ('pink')
        self.configure(background=corFundo)
        # Colocando um título na Janela
        self.title('Exibir Itens')
        self.transient(parent)
        self.grab_set()

        #Widgets
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        # Posicionando os widgets:
        self.btn_close.place(x=10, y=120)

    # Método para ativar o Button 'Sair':
    def destroy(self):
        # Janela de confirmação para fechar:
        if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
            super().destroy()