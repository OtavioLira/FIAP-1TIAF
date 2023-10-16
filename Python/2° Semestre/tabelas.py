import os
# Criando um dicionário
dados = {
    # key  : Value
    'nome': 'Edson de Oliveira',
    'idade': 49,
    'cep': '012212'
}

os.system("clear")
# exibi o dicionario
print(dados)
# criei uma lista vazia
tabela = list()
# acrescentei o dicionario na lista|tabela
tabela.append(dados.copy())
# exibi o conteudo da tabela
print(tabela)

# modifiquei os dados do dicionario
dados['nome'] = 'Maria'
dados['idade'] = 23

# inseri na tabela os novos dados
tabela.append(dados.copy())

print(tabela)

for k in dados.keys():  # keys, pega todas as keys (campos) do dicionario
    print(k)

for v in dados.values():  # keys, pega todas as keys (campos) do dicionario
    print(v)

for k, v in dados.items():
    print(f"{k}....: {v}")
    
 """
 Exercícios:
 CRIAR UM DICIONARIO COM AO MENOS 4 CAMPOS (KEYS) - o primeiro campo deve ser nome
 1. Fazer um procedimento que preencha uma tabela até que seja digitado ponto no Nome.
 2. Fazer um procedimento que exiba o conteudo da tabela.
 
 CRIE UM MENU COM DOIS ITEMS
 """
