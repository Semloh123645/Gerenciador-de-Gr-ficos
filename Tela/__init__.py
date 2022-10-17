from tkinter import *
import tkinter.font as tkFont
# from ttkbootstrap import Style
from functools import partial
from Plots import pegar_Graficos, restart_program
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt
import os
from tkinter import messagebox
import numpy as np

teste = list()
teste1 = list()
name1 = list()
name2 = list()
arquivo1 = list()
subplots = list()

'''for i in range(0, 2):
    a = np.arange(1, 6)
    dados = np.random.randint(20, 30, 5)
    print(dados)
    print(a)
    plt.clf()
    plt.cla()
    plt.ion()
    plt.plot(a, dados)
    plt.pause(2)'''

# plt.ioff()

def iteration(x):
    arq = open(x)
    linhas = arq.readlines()
    teste.clear()
    teste1.clear()
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


def plot1(y):
    iteration(y)
    plt.cla()
    plt.clf()

    plt.ion()
    plt.plot(teste, teste1)
    plt.ylabel(name2[1])
    plt.xlabel(name1[1])
    plt.pause(2)

    plt.grid(True)
    plt.ioff()
    # plt.show()


def pegar_Graficos(path=''):
    try:
        pasta = fr'{path}'
        print(pasta)
        arquivos = os.listdir(pasta)
        for i in arquivos:
            if i.split('.')[-1] == 'txt':
                plot1(rf'{pasta + "/" + i}')
    except:
        print("caminho inválido")


# pegar_Graficos(r'E:\programacao\Python files\python\Daniel Projeto Concluso - Copia\Glicerol-T5\Glicerol-T5')
a = 'T5.B-I(d).txt'
print(a.replace('(', ' ('))
