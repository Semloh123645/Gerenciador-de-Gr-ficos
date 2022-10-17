from tkinter import *
import tkinter.font as tkFont
from functools import partial
import matplotlib.pyplot as plt
import os
from Treeview_test import Treeview

teste = list()
teste1 = list()
name1 = list()
name2 = list()
arquivo1 = list()
subplots = list()


class Program:
    def __init__(self):
        pass

    def iteration(self, x):
        teste.clear()
        teste1.clear()
        arq = open(x)
        linhas = arq.readlines()
        for linha in linhas:
            try:
                trans1 = linha.split()[0].replace(',', '.')
                trans2 = linha.split()[1].replace(',', '.')
                teste.append(float(trans1))
                teste1.append(float(trans2))
            except:
                name1.append(trans1)
                name2.append(trans2)

        arq.close()

    def plot1(self, y, title):
        Program.iteration(self, y)

        plt.plot(teste, teste1)
        plt.ylabel(name2[1])
        plt.xlabel(name1[1])

        plt.grid(True)
        plt.title(title)
        plt.show()

    def pegar_Graficos(self, path=''):

        try:
            pasta = fr'{path.get()}'
            arquivos = os.listdir(pasta)
            for i in arquivos:
                if i.split('.')[-1] == 'txt':
                    arquivo1.append(i)
        except:
            print("caminho inválido")

        self.count = 0
        while self.count <= len(arquivo1):
            if arquivo1[self.count].split('.')[-1] == 'txt':
                Program.plot1(self, rf'{pasta + "/" + arquivo1[self.count]}', arquivo1[self.count])
                # try:
                if self.ce_nome.get() == "break":
                    self.ce_nome.delete([0], [len(self.ce_nome.get())])
                    break

                elif self.ce_nome.get() == "a":
                    self.count -= 1
                    self.ce_nome.delete([0], [len(self.ce_nome.get())])

                elif self.ce_nome.get() == "b":
                    self.count += 1
                    self.ce_nome.delete([0], [len(self.ce_nome.get())])
            # except:
                else:
            #     plt.close()
                    break

    def previous(self):
        self.ce_nome.delete([0], [len(self.ce_nome.get())])
        self.ce_nome.insert([0], 'a')
        plt.close()
        # self.ce_nome.delete([0], [len(self.ce_nome.get())])

    def next(self):
        self.ce_nome.delete([0], [len(self.ce_nome.get())])
        self.ce_nome.insert([0], 'b')
        plt.close()
        # self.ce_nome.delete([0], [len(self.ce_nome.get())])

    def quit(self):
        try:
            self.ce_nome.delete([0], [len(self.ce_nome.get())])
            self.ce_nome.insert([0], 'break')
            plt.close()
        except:
            self.ce_nome.delete([0], [len(self.ce_nome.get())])

    def Tela(self):
        janela = Tk()
        janela.title("Gerenciador de Gráficos")
        janela.geometry('600x650+390+30')
        janela.config(background='blue')

        fontExample = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic")
        fontExample1 = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")

        lb_nome = Label(janela, text='Set the path:', font=fontExample, bg='blue', fg="white")
        self.ce_nome = Entry(janela, width=50)

        bt0 = Button(janela, width=12, text='Plot', font=fontExample, bg="green")
        bt0['command'] = partial(Program.pegar_Graficos, self, self.ce_nome)

        bt1 = Button(janela, width=6, text='Next', font=fontExample)
        bt1['command'] = partial(Program.next, self)

        bt2 = Button(janela, width=10, text='Previous', font=fontExample)
        bt2['command'] = partial(Program.previous, self)

        bt3 = Button(janela, width=12, text='Stop', font=fontExample, bg="red")
        bt3['command'] = partial(Program.quit, self)

        bt4 = Button(janela, width=10, text='Comparing', font=fontExample1, fg="black")
        bt4['command'] = partial(Treeview.frame, self, janela)

        lb_nome.place(x=255, y=120)
        self.ce_nome.place(x=155, y=170)

        bt0.place(x=230, y=300)
        bt1.place(x=350, y=350)
        bt2.place(x=150, y=350)
        bt3.place(x=230, y=400)
        bt4.place(x=440, y=50)

        janela.mainloop()


Program().Tela()
