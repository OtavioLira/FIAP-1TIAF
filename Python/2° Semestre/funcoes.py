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


# ------------ TESTES DOS SUBALGORITMOS
if __name__ == "__main__":
    os.system("clear")
    #                   -4  -3    -2    -1
    #                   0   1     2      3
    nome_completo = "Edson de Oliveira Silva"
    nome_sobrenome(nome_completo)
    qtd_palavras = conta_palavras(nome_completo)
    print(qtd_palavras)
    print(nome_bibliografia(nome_completo))
