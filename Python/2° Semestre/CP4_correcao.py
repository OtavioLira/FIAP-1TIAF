import os

# ------------ DEFINIÇÃO DOS SUBALGORITMOS
# Item 2 - Exibe separado o Nome do Sobrenome


def nome_sobrenome(nc: str) -> None:
    lista_nome = nc.split()
    print(f"\nNome: {lista_nome[0]}")
    sobrenome = " ".join(lista_nome[1:])
    print(f"Sobrenome: {sobrenome}\n")

# Item 3 - Conta quantas palavras há no nome completo


def conta_palavras(nc: str) -> int:
    lista_nome = nc.split()
    return len(lista_nome)

# Item 4 - Exibir em formato de bibliografia
# SILVA, Edson de Oliveira


def nome_bibliografia(nc: str) -> str:
    lista_nome = nc.split()
    ultimo_nome = lista_nome[-1].upper()
    parte_nome = " ".join(lista_nome[0:-1])
    return ultimo_nome + ', ' + parte_nome


# ------------ PROGRAMA PRINCIPAL
nome_preenchido = False
nome_completo = ""
margem = " "*4
while True:
    os.system("clear")
    print("""
    MENU

    0 - SAIR
    1 – Digite um nome completo
    2 – Exibe separado o Nome do Sobrenome
    3 – Conta quantas palavras há no nome completo
    4 – Exibir em formato de bibliografia 
    """)
    opcao = input(margem + "Escolha: ")
    while not opcao.isnumeric():  # enquanto nao for digitado um valor numerico
        print(margem + "Opção inválida, digite um valor numérico!")
        opcao = input(margem + "Escolha: ")
    opcao = int(opcao)

    match opcao:
        case 0:
            break
        case 1:
            nome_completo = input("\n" + margem + "Digite um nome completo: ")
            if nome_completo != "":
                nome_preenchido = True
            else:
                nome_preenchido = False
        case 2:
            if nome_preenchido:
                nome_sobrenome(nome_completo)
            else:
                print(margem + "Primeiramente digite um nome na opção 1.")
        case 3:
            if nome_preenchido:
                print(
                    f"O nome {nome_completo} tem {conta_palavras(nome_completo)} palavras.")
            else:
                print(margem + "Primeiramente digite um nome na opção 1.")
        case 4:
            if nome_preenchido:
                print(nome_bibliografia(nome_completo))
            else:
                print(margem + "Primeiramente digite um nome na opção 1.")
        case _:
            print(margem + "Opção inválida, digite um item de 0 a 4.")
    input("\n" + margem + "==> Digite algo para continuar...")


# ------------ TESTES DOS SUBALGORITMOS
"""
os.system("clear")
#                   -4  -3    -2    -1
#                   0   1     2      3
nome_completo = "Edson de Oliveira Silva"
nome_sobrenome(nome_completo)
qtd_palavras = conta_palavras(nome_completo)
print(qtd_palavras)
print(nome_bibliografia(nome_completo))


'''
0 Edson
1 de
2 Oliveira
3 Silva
'''
"""
