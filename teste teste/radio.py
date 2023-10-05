from tkinter import *

# def sel():
#    selection = "You selected the option " + str(var.get())
#    label.config(text = selection)
# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
# R1.pack( anchor = W )
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
# R2.pack( anchor = W )
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
# R3.pack( anchor = W)
# label = Label(root)
# label.pack()
# root.mainloop()

#-----IMPORTS-----
import requests
import json
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

url = requests.get('https://economia.awesomeapi.com.br/json/all')

url_dic = url.json()
#-----DIA-----
dolar = url_dic['USD']['bid']
euro = url_dic['EUR']['bid']
bt = url_dic['BTC']['bid']

# -----SEMANA dolar-----
USDcotacao_din7d = requests.get('https://economia.awesomeapi.com.br/daily/USD-BRL/7')
USDcotacao_din7d_dic = USDcotacao_din7d.json()
USDlista_cotacao_dolar7d = [float(item['bid']) for item in USDcotacao_din7d_dic]
print(USDlista_cotacao_dolar7d)

# -----MES dolar-----
USDcotacao_din30d = requests.get('https://economia.awesomeapi.com.br/daily/USD-BRL/30')
USDcotacao_din30d_dic = USDcotacao_din30d.json()
USDlista_cotacao_dolar30d = [float(item['bid']) for item in USDcotacao_din30d_dic]
print(USDlista_cotacao_dolar30d)


# -----SEMANA euro-----
EURcotacao_din7d = requests.get('https://economia.awesomeapi.com.br/daily/EUR-BRL/7')
EURcotacao_din7d_dic = EURcotacao_din7d.json()
EURlista_cotacao_euro7d = [float(item['bid']) for item in EURcotacao_din7d_dic]
print(EURlista_cotacao_euro7d)

# -----MES euro-----
EURcotacao_din30d = requests.get('https://economia.awesomeapi.com.br/daily/EUR-BRL/30')
EURcotacao_din30d_dic = EURcotacao_din30d.json()
EURlista_cotacao_euro30d = [float(item['bid']) for item in EURcotacao_din30d_dic]
print(EURlista_cotacao_euro30d)



# -----SEMANA bitcoin-----

BTCcotacao_din7d = requests.get('https://economia.awesomeapi.com.br/daily/BTC-BRL/7')
BTCcotacao_din7d_dic = BTCcotacao_din7d.json()
BTClista_cotacao_btc7d = [float(item['bid']) for item in BTCcotacao_din7d_dic]
print(BTClista_cotacao_btc7d)

# -----MES bitcoin-----
BTCcotacao_din30d = requests.get('https://economia.awesomeapi.com.br/daily/BTC-BRL/30')
BTCcotacao_din30d_dic = BTCcotacao_din30d.json()
BTClista_cotacao_btc30d = [float(item['bid']) for item in BTCcotacao_din30d_dic]
print(BTClista_cotacao_btc30d)



#-----TK-----

raiz = tk.Tk()
raiz.title('Cotação Moedas')
raiz.geometry('600x400')

def mostrar_grafico():

    #-----BOTAO DE CHECK-----

    selecao_moeda = sel_moeda.get()
    selecao_dias = sel_periodo.get()



    #-----SEMANA DOLAR-----
    # if Dolar and semana == 1:
    if sel_moeda==1 and sel_periodo==1:
        figura = plt.Figure(figsize=(8, 4), dpi=60)
        ax = figura.add_subplot(111)
        ax.plot(USDlista_cotacao_dolar7d)
        ax.set_title('DOLAR - 7 DIAS')
        canva = FigureCanvasTkAgg(figura, raiz)
        canva.get_tk_widget().pack()

    #-----MES DOLAR-----
    if sel_moeda==1 and sel_periodo==2: 
        figura = plt.Figure(figsize=(8, 4), dpi=60)
        ax = figura.add_subplot(111)
        ax.plot(USDlista_cotacao_dolar30d)
        ax.set_title('DOLAR - 30 DIAS')
        canva = FigureCanvasTkAgg(figura, raiz)
        canva.get_tk_widget().pack()

    #-----SEMANA EURO-----
    if sel_moeda==2 and sel_periodo==1:
        figura = plt.Figure(figsize=(8, 4), dpi=60)
        ax = figura.add_subplot(111)
        ax.plot(EURlista_cotacao_euro7d)
        ax.set_title('EURO - 7 DIAS')
        canva = FigureCanvasTkAgg(figura, raiz)
        canva.get_tk_widget().pack()

    #-----MES EURO-----
    if sel_moeda==2 and sel_periodo==2:
        figura = plt.Figure(figsize=(8, 4), dpi=60)
        ax = figura.add_subplot(111)
        ax.plot(EURlista_cotacao_euro30d)
        ax.set_title('EURO - 30 DIAS')
        canva = FigureCanvasTkAgg(figura, raiz)
        canva.get_tk_widget().pack()

    #-----SEMANA BTC-----
    if sel_moeda==3 and sel_periodo==1:
        figura = plt.Figure(figsize=(8, 4), dpi=60)
        ax = figura.add_subplot(111)
        ax.plot(BTClista_cotacao_btc7d)
        ax.set_title('BITCOIN - 7 DIAS')
        canva = FigureCanvasTkAgg(figura, raiz)
        canva.get_tk_widget().pack()

    #-----MES BTC-----
    if sel_moeda==3 and sel_periodo==2:
        figura = plt.Figure(figsize=(8, 4), dpi=60)
        ax = figura.add_subplot(111)
        ax.plot(BTClista_cotacao_btc30d)
        ax.set_title('BITCOIN1 - 30 DIAS')
        canva = FigureCanvasTkAgg(figura, raiz)
        canva.get_tk_widget().pack()

    else:
        print('Selecione uma opção')

    
sel_moeda = tk.IntVar()
sel_periodo = tk.IntVar()


#----TITULO DO TK----
titulo = tk.Label(raiz, text='Selecione a moeda:')
titulo.pack()

#-----Dólar-----
Dolar = tk.Radiobutton(raiz, text='Dólar: {}'.format(dolar), variable = sel_moeda, value=1)
Dolar.pack()
print(sel_moeda)

#-----Euro-----
Euro = tk.Radiobutton(raiz, text='Euro: {}'.format(euro), variable = sel_moeda, value=2)
Euro.pack()
print(sel_moeda)

#-----Bitcoin-----
Btc = tk.Radiobutton(raiz, text='Bitcoin: {}'.format(bt), variable = sel_moeda, value=3)
Btc.pack()
print(sel_moeda)

titulo = tk.Label(raiz, text='Selecione o período: ')
titulo.pack()

#-----Gráfico7d-----
semana = tk.Radiobutton(raiz, text='7 Dias', variable = sel_periodo, value=1)
semana.pack()

#-----Gráfico30d-----
mes = tk.Radiobutton(raiz, text='30 Dias', variable = sel_periodo, value=2)
mes.pack()

#-----Botões-----
botao = tk.Button(raiz, text = 'Ver gráfico', command = mostrar_grafico)
botao.pack()

# botao2 = tk.Button(raiz, text = 'Limpar', command = limpar)
# botao2.pack()


raiz.mainloop()