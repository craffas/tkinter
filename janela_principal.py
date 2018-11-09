#Importando as bibliotecas:
from tkinter import *
from tkinter import messagebox
from segunda_janela import Segunda_Janela

#Classe janela_principal
class Janela_Principal(Tk):
    #Método Construtor
    def __init__(self, controle):
        #Atributos:
        self.controle = controle
        #Executar o método da classe mãe:
        super().__init__()
        #Ajustar tamanho
        self.geometry('380x440+50+100')
        #Definindo cor de fundo da tela:
        corFundo = ('pink')
        self.configure(background=corFundo)
        #Colocando um título na Janela
        self.title('Lista de Compras')

        #Widgets na tela:
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='Ok', command=self.btn_ok_click)
        self.lbl_ok = Label(self, text='USUÁRIO', background=corFundo, font='Arial')
        self.txt_ok = Entry(self)
        self.lbl_senha_ok = Label(self, text='SENHA', background=corFundo, font='Arial')
        self.txt_senha_ok = Entry(self, show='*')

        #Criando exibição de itens na tela:
        self.exb = Label(self, text='')
        self.exb_msg = Label(self, text='Itens na lista:')
        #Posicionando os widgets:
        self.btn_close.place(x=140, y=300)
        self.btn_ok.place(x=140, y=260)
        self.lbl_ok.place(x=145, y=90)
        self.txt_ok.place(x=120, y=120)

        self.lbl_senha_ok.place(x=145, y=160)
        self.txt_senha_ok.place(x=120, y=190)
        # == Menu ==
        #Criando um menu:
        self.menu = Menu(self)
        #Criando item e subitens de menu:
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Exibir Item',command=self.criar_segunda_janela)
        self.menu_principal.add_command(label='Adicionar Item', command=self.menu_click)
        self.menu_principal.add_command(label='Excluir Item', command=self.menu_click)
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair', command=self.destroy)

        #Mostrando o menu:
        self.config(menu=self.menu_principal)

    #Método para ativar o Button 'Sair':
    def destroy(self):
        #Janela de confirmação para fechar:
        if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
            super().destroy()

    #Método para btn_ok
    def btn_ok_click(self):
        #Recuperar a lista de compra:
        lista_compra = self.controle.get_lista_compra()
        #Percorrer a lista:
        for item in lista_compra:
            messagebox.showinfo('Item', item.to_string())

    #Método para clicar no item de menu:
    def menu_click(self):
        messagebox.showinfo('Menu', 'Clicou no item de menu')

    #Método para criar a segunda janela:
    def criar_segunda_janela(self):
        Segunda_Janela(self)

    #Método para exibir a lista:
    def exibir_na_tela(self):
        #Redimensionando na tela:
        self.exb_msg.place(x=10, y=60)
        self.exb.place(x=10, y=80)

