# # API
# O que é uma api?
# API's são mecanismo que permitem dois componentes se comunicarem com outro dentro de um software
# Um exemplo: Em um restaurante o cliente não vai na cozinha pedir diretamente pro chefe fazer seu prato, quem faz isso é o garçom, ele seria a nossa 'API'.
# Outro exemplo Por exemplo, o sistema de software do instituto meteorológico contém dados meteorológicos diários. A aplicação para a previsão do tempo em seu telefone “fala” com esse sistema por meio de APIs e mostra atualizações meteorológicas diárias no telefone.
# 
# As API´s conseguem fazer isso usando um conjunto de definições e protocolos

# %%
import requests
from tkinter import *

def pegar_cotações():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    contacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {contacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_resposta['text'] = texto

#Criar a janela
janela = Tk()
janela.title("Cotação atual das moedas")
janela.iconbitmap("./icons8-python.ico")
#Texto Cotações
texto = Label(janela, text = "Clique no botão para ver as cotações")
texto.grid(column=0, padx=10, pady= 10, row=0)

# Botão para exibir as cotações
botao = Button(janela, text="Buscar cotações", command=pegar_cotações)
botao.grid(column=0, padx=10, pady=10, row=1)

#Texto resposta das cotações
texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, padx=10, pady=10, row=2)

#Manter a janela rodando
janela.mainloop()

# %% [markdown]
# 
# Explore a biblioteca Tkinter e faça um programa (com funções) que calcule o delta a partir de 3 valores A, B e c fornecidos pelo usuário

# %%
import requests
from tkinter import *

def calcular_delta():
    A = float(valorA.get())
    B = float(valorB.get())
    C = float(valorC.get())
    
    delta = (B**2) - (4 * A * C)
    X1 = (((-1) * B) + (delta**0.5)) / (2 * A)
    X2 = (((-1) * B) - (delta**0.5)) / (2 * A)

    if delta == 0:
        texto = f'''
        Equação do 2º Grau: 
        A: {A}
        B: {B}
        C: {C}
        Delta = 0, temos um único valor de raiz (x1 = x2): 
        {X1}'''
        texto_resposta['text'] = texto
    elif delta > 0:
        texto = f'''
        Equação do 2º Grau: 
        A: {A}
        B: {B} 
        C: {C}
        Delta > 0, temos dois valores distintos de raízes: 
        {X1}, {X2}'''
        texto_resposta['text'] = texto
    else:
        texto = f'''
        Equação do 2º Grau: 
        A: {A} 
        B: {B} 
        C: {C}
        Delta < 0, não temos raízes reais'''
        texto_resposta['text'] = texto

# Criar a janela
janela = Tk()
janela.title("Calcular Delta")
janela.iconbitmap("./icons8-python.ico")

# Entradas
textoVA = Label(janela, text="Valor de A ").grid(column=0, row=1)
valorA = Entry(janela)
valorA.grid(column=1, row=1)

textoVB = Label(janela, text="Valor de B ").grid(column=0, row=2)
valorB = Entry(janela)
valorB.grid(column=1, row=2)

textoVC = Label(janela, text="Valor de C ").grid(column=0, row=3)
valorC = Entry(janela)
valorC.grid(column=1, row=3)

# Botão para calcular
botao = Button(janela, text="Calcular Delta", command=calcular_delta)
botao.grid(column=0, padx=10, pady=10, row=4)

# Texto resposta
texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, padx=10, pady=10, row=5)

# Manter a janela rodando
janela.mainloop()

# %% [markdown]
# Testes que podem ser feitos
# 
# **Teste 1**
# 
# A = 2, B = 8, C = -24 
# 
# Delta > 0, temos dois valores distintos de raízes
# 
# **Teste 2**
# 
# A = 1, B = 2, C = 3
# 
# Delta < 0, Não temos raizes reais


