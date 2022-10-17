import matplotlib.pyplot as plt
import os

teste = list()
teste1 = list()
name1 = list()
name2 = list()
name3 = list()
name4 = list()
a = list()
b = list()


def iteration(path, x):

    arq = open(rf'{path + "/" + x}')
    linhas = arq.readlines()
    teste.clear()
    teste1.clear()
    name1.clear()
    name2.clear()
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


def process(path, y):
    a = plt.figure()
    if len(y) <= 2:
        for index, items in enumerate(y):
            iteration(path, items)

            a = plt.subplot(2, 1, (index+1))
            a.plot(teste, teste1)

            plt.subplots_adjust(hspace=0.55)

            a.grid(True)
            a.set_title(f'{items}')

            plt.ylabel(name2[1])
            plt.xlabel(name1[1])

    elif len(y) <= 4:
        a.set_figwidth(16)
        a.set_figheight(5.8)
        for index, items in enumerate(y):
            iteration(path, items)

            a = plt.subplot(2, 2, (index+1))
            a.plot(teste, teste1)

            plt.subplots_adjust(hspace=0.55)

            a.grid(True)
            a.set_title(f'{items}')

            plt.ylabel(name2[1])
            plt.xlabel(name1[1])

    elif 4 < len(y) <= 6:
        a.set_figwidth(16)
        a.set_figheight(5.8)
        for index, items in enumerate(y):
            iteration(path, items)

            a = plt.subplot(3, 2, (index + 1))
            a.plot(teste, teste1)

            plt.subplots_adjust(hspace=0.88)

            a.grid(True)
            a.set_title(f'{items}')

            plt.ylabel(name2[1])
            plt.xlabel(name1[1])
    plt.show()


def subplots(path, list):
    try:
        pasta = fr'{path}'
        arquivos = os.listdir(pasta)
    except:
        print("caminho inválido")
    a.clear()
    for files in list:
        a.append(arquivos.index(files.replace("(", ' (')))

    for c in a:
        b.append(arquivos[c])
    arquivos.clear()
    process(path, b)
    b.clear()
