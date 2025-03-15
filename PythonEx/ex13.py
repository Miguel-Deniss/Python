nome = 'Miguel'
altura = 1.77 #Metros
peso = 60 #Kg
imc = peso / altura ** 2

#F-Strings
linha_1 = f'{nome} tem altura de {altura:.2f} e pesa {peso} Kg'
linha_2 = f'Seu imc é :{imc:.2f}'

print(linha_1)
print(linha_2)