def ingredientes() -> list:
    ingredientes = [
        ["arroz", 1000, 100, '30/06/2023'],   # Lista de ingredientes com suas informações
        ["feijão", 500, 100, '02/06/2023'],   # nome, quantidade disponivel, porcao, data de validade
        ["carne", 1000, 200, '05/06/2023'],
        ["salada", 500, 50, '15/06/2023']
    ]
    return ingredientes

def verificar_validade(data_validade: str) -> bool:
    data_validade = str(data_validade)   # Conversão para string (caso não seja)
    # Data atual
    dia_atual = 4
    mes_atual = 6
    ano_atual = 2023
    # Prazo de validade do ingrediente
    dia = int(data_validade[0:2])   # Extração do dia da data de validade
    mes = int(data_validade[3:5])   # Extração do mês da data de validade
    ano = int(data_validade[6:])    # Extração do ano da data de validade
    # Essa condição verifica se o ingrediente está dentro do prazo
    if ano_atual <= ano and mes_atual <= mes and dia_atual <= dia:
        return True  # Dentro do prazo
    return False  # Fora do prazo

def criar_cardapio(pessoas, refeicoes, ingredientes) -> list:
    cardapio = []
    for ingrediente in ingredientes:
        if verificar_validade(ingrediente[3]): # Verificar se o ingrediente está dentro do prazo
            quantidade_disponivel = ingrediente[1] # Verificar a quantidade disponível de cada ingrediente
            porcao = ingrediente[2] # Obter a porção utilizada para cada cliente
            total_porcoes = refeicoes * porcao # Calcular o total de porções para a quantidade de refeições
            if quantidade_disponivel >= total_porcoes: # Verificar se há ingredientes suficientes
                cardapio.append([ingrediente[0], total_porcoes]) # Adicionar o ingrediente ao cardápio com a quantidade total de porções
            else:
                quantidade_possivel = quantidade_disponivel // porcao # Calcular a quantidade possível de porções com base na quantidade disponível
                cardapio.append([ingrediente[0], quantidade_possivel]) # Adicionar o ingrediente ao cardápio com a quantidade possível de porções
        else:
            print("\nIngredientes fora da validade!")
            print(ingrediente[0] + " validade: " + ingrediente[3])
    return cardapio

def main() -> None:
    print("\nBem-vindo ao Restaurante CardapioTop:")
    pessoas = int(input("Quantidade de pessoas a serem alimentadas: ")) # obter a quantidade de pessoas
    refeicoes = int(input("Quantidade de refeições a serem produzidas: ")) # obter a quantidade de refeicoes
    lista_ingredientes = ingredientes() # obter a lista de ingredientes
    for ingrediente in lista_ingredientes:
        print(f"Ingrediente: {ingrediente[0]}")
        quantidade = int(input("Digite a quantidade do ingrediente: ")) # solicitar a quantidade de cada ingrediente
        validade = input("Digite a validade dos ingredientes (dd/mm/aaaa): ") # Solicitar a quantidade de cada ingrediente
        ingrediente[1] = quantidade # Atualizar a quantidade do ingrediente na lista
        ingrediente[3] = validade # Atualizar a validade do ingrediente na lista

    cardapio = criar_cardapio(pessoas, refeicoes, lista_ingredientes) # Criar o cardápio com base nas informações fornecidas
    print("\nCardapioTop Total:")
    for item in cardapio:
        print(f"{item[0]}: {item[1]}g") # Exibir o cardápio final com os ingredientes e suas quantidades
        
main()
