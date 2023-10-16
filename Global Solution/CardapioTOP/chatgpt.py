from datetime import datetime

def verificar_validade(data_validade):
    data_atual = datetime.now().date()
    if data_validade < data_atual:
        return False
    return True

def criar_cardapio(pessoas, refeicoes, ingredientes):
    cardapio = {}
    for ingrediente, quantidade in ingredientes.items():
        if verificar_validade(quantidade["validade"]):
            quantidade_disponivel = quantidade["quantidade"]
            porcao = quantidade["porcao"]
            total_porcoes = pessoas * refeicoes
            if quantidade_disponivel >= total_porcoes * porcao:
                cardapio[ingrediente] = total_porcoes
            else:
                cardapio[ingrediente] = quantidade_disponivel // porcao

    return cardapio

# Exemplo de uso
pessoas = int(input("Quantidade de pessoas a serem alimentadas: "))
refeicoes = int(input("Quantidade de refeições a serem produzidas: "))

ingredientes = {
    "arroz": {
        "quantidade": 1000,
        "porcao": 100,
        "validade": datetime(2023, 6, 30).date()
    },
    "feijão": {
        "quantidade": 500,
        "porcao": 100,
        "validade": datetime(2023, 6, 2).date()
    },
    "carne": {
        "quantidade": 1000,
        "porcao": 200,
        "validade": datetime(2023, 6, 5).date()
    },
    # Adicione outros ingredientes aqui
}

cardapio = criar_cardapio(pessoas, refeicoes, ingredientes)

print("\nCardápio:")
for ingrediente, quantidade in cardapio.items():
    print(f"{ingrediente}: {quantidade}g")
