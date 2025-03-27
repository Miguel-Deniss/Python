# operadores lógicos
# and (e) -> todas as condições devem ser verdadeiras
# or (ou) -> pelo menos uma das condições deve ser verdadeira
# not (não) -> inverte o resultado, se for verdadeiro, torna falso e vice-versa
# none -> não tem valor
# 0 0.0 '' -> false

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_salva = '123456'

if entrada == 'E' and senha_digitada == senha_salva:
  print('Entrou')
else:
  print('Saiu')























