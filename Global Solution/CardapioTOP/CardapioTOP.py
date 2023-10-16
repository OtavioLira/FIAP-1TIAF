def ingredientes() -> list:
    ingredientes = [
        ["arroz", 1000, 100, '30/06/2023'],
        ["feijão", 500, 100, '02/06/2023'],
        ["carne", 1000, 200, '05/06/2023'],
        ["salada", 500, 50, '15/06/2023']
    ]
    return ingredientes

def verificar_validade(data_validade: str) -> bool:
    data_validade = str(data_validade)
    # Data atual
    dia_atual = 4
    mes_atual = 6
    ano_atual = 2023
    # Prazo de validade do ingrediente
    dia = int(data_validade[0:2])
    mes = int(data_validade[3:5])
    ano = int(data_validade[6:])
    # Essa condição verifica se o ingrediente está dentro do prazo
    if ano_atual <= ano and mes_atual <= mes and dia_atual <= dia:
        return True  # Dentro do prazo
    return False  # Fora do prazo

def criar_cardapio(pessoas, refeicoes, ingredientes) -> list:
    cardapio = []
    for ingrediente in ingredientes:
        if verificar_validade(ingrediente[3]):
            quantidade_disponivel = ingrediente[1]  # verificar a quantidade disponível de cada ingrediente
            porcao = ingrediente[2]  # porção que usamos para cada cliente
            total_porcoes = refeicoes * porcao  # porções para cada boca a serem alimentadas
            print(ingrediente)
            print(total_porcoes)
            # Verificar a quantidade disponível dos ingredientes
            if quantidade_disponivel >= total_porcoes:
                cardapio.append([ingrediente[0], total_porcoes])
            else:  # caso não tenha ingredientes suficientes
                # a quantidade de porções será dividida
                print("Não tem quantidade de ingredientes disponivel")
                print("A porcao sera diminuida")
                #cardapio.append([ingrediente[0], quantidade_disponivel // pessoas])
        else:  # avisar caso algum ingrediente esteja fora da validade
            print("\ningredientes fora da validade!")
            print(ingrediente[0] + " validade: " + ingrediente[3])
    return cardapio

def main() -> None:
    print("\nBem-vindo ao Restaurante CardapioTop:")
    pessoas = int(input("Quantidade de pessoas a serem alimentadas: "))
    refeicoes = int(input("Quantidade de refeições a serem produzidas: "))
    lista_ingredientes = ingredientes()
    for ingrediente in lista_ingredientes:
        print(f"Ingrediente: {ingrediente[0]}")
        quantidade = int(input("Digite a quantidade do ingrediente: "))
        validade = str(input("digite a validade dos ingredientes (dd/mm/aaaa): "))
        ingrediente[1] = quantidade
        ingrediente[3] = validade

    cardapio = criar_cardapio(pessoas, refeicoes, lista_ingredientes)
    # Exibir o cardápio
    print("\nCardapioTop Total:")
    for item in cardapio:
        print(f"{item[0]}: {item[1]}g")
main()
