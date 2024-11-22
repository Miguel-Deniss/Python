from datetime import datetime

# Função para calcular a idade a partir da data de nascimento
def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Lista para armazenar as informações das pessoas
pessoas = []

# Coletando informações de 5 pessoas
for i in range(5):
    print(f"\nPessoa {i + 1}:")
    genero = input("Digite o gênero (M/F): ")
    data_nascimento_str = input("Digite a data de nascimento (dd/mm/aaaa): ")
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    idade = calcular_idade(data_nascimento)
    
    pessoas.append({"genero": genero, "idade": idade, "data_nascimento": data_nascimento})

# Ordenando as pessoas pela idade
pessoas.sort(key=lambda x: x['idade'])

# Exibindo as informações em ordem crescente de idade
print("\nPessoas em ordem crescente de idade:")
for pessoa in pessoas:
    print(f"Gênero: {pessoa['genero']}, Idade: {pessoa['idade']}, Data de Nascimento: {pessoa['data_nascimento'].strftime('%d/%m/%Y')}")