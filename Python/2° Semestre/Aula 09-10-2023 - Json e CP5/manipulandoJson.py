import os
os.system("cls")
pessoas = {
    'pessoa_1': {
        'Nome': 'Otavio',
        'Idade': 19
    },
    'pessoa_2': {
        'Nome' : 'Jorge',
        'Idade': '?'
    }
}

#importar o framework json
import json


# Cria um objeto pessoa_json
pessoas_json = json.dumps(pessoas, indent=4)

print(f"Dicionario: {pessoas}")
print()
print(f"Objeto json: {pessoas_json}")

# Abrindo um arquivo json para gravação
with open("arquivo.json", "w+") as file:
    # Gravando o objeto json no arquivo
    file.write(pessoas_json)

# Lendo um arquivo json
with open("arquivo.json", "r") as file:
    file.seek(0)
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)


print(f"Dicionario: {pessoas}")
print()
print(f"Objeto json: {pessoas_json}")

# Formatando os dados para o usuário
print(f"Formatando os dados para o usuário: ")
for k, v in pessoas.items():
    print(f"Registro......{k}")
    for k1, v1 in v.items():
        print(f"\t{k1} : {v1}")
    