from tkinter import *
import tkinter.font as tkFont
from functools import partial
import os
from tkinter import ttk
from Iterative import subplots

compare = list()


class Treeview:
    def __init__(self):
        pass

    def frame(self, janela):
        self.frame1 = Frame(janela, width=600, height=650, bg='purple')
        self.frame1.place(x=0, y=0)
        Treeview.Treeview(self, self.frame1)

        lb_nome = Label(self.frame1, text='Set the path:', bg='purple', fg='white', font=14)
        ce_nome = Entry(self.frame1, width=50)
        lb_nome.place(x=50, y=20)
        ce_nome.place(x=140, y=20)

        bt0 = Button(self.frame1, width=12, text='Search', bg="green", fg="white", font=14)
        bt0.place(x=450, y=15)
        bt0['command'] = partial(Treeview.treeview_files, self, ce_nome)

        bt1 = Button(self.frame1, width=12, text='Plot', bg="green", fg="white", font=14)
        bt1.place(x=260, y=600)
        bt1['command'] = partial(Treeview.comparing, self)

        bt2 = Button(self.frame1, width=12, text='Back', bg="red", fg="white", font=14)
        bt2.place(x=100, y=600)
        bt2['command'] = partial(self.frame1.place_forget)

    def Treeview(self, frame):
        fontExample = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")
        fontExample1 = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic")

        omni = ttk.Style()
        omni.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                       font=(fontExample))  # Modify the font of the body
        omni.configure("mystyle.Treeview.Heading", font=fontExample1, rowheight=40)  # Modify the font of the headings
        omni.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.dados = ttk.Treeview(frame, style="mystyle.Treeview", columns=[1], show='headings', height=25)
        self.dados.column(1, width=200)
        self.dados.heading(1, text='Files')
        self.dados.bind('<<TreeviewSelect>>')
        self.dados.place(x=50, y=50)

    def treeview_files(self, path=''):
        try:
            self.pasta = fr'{path.get()}'
            arquivos = os.listdir(self.pasta)
            for i in arquivos:
                if i.split('.')[-1] == 'txt':
                    self.dados.insert('', 'end', values=(i.replace(' ', '')))
                    print(i)
                else:
                    pass
        except:
            print("caminho inválido")

    def comparing(self):
        compare.clear()
        data = (self.dados.selection())
        for item in data:
            current_item = self.dados.item(item)
            current_value = current_item.get("values")
            compare.append(current_value[0])
        subplots(self.pasta, compare)

