import os
from funcoes import conta_palavras, nome_sobrenome, nome_bibliografia

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
