# If   / elif      / else
# Se / Se não se / Se não
entrada = input('Você quer "Entrar" ou "Sair"? ')

#primeira opção
if entrada == 'Entrar':
  print('Você entrou no local')

#segunda opção
elif entrada == 'Sair':
    print('Você saiu do local')

#terceira quando necessario
else:
    print('Você não digitou nenhuma das opções acima')