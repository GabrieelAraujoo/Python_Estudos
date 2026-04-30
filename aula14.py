# Operadores lógicos

# and (e) -> todas as condições precisam ser verdadeiras
# or (ou) -> pelo menos uma condição precisa ser verdadeira
# not (não) -> inverte o valor lógico

senha = '123'
login = input('Digite sua senha: ')
entrada = input('[E]ntrar [S]air: ')

if entrada == 'E' and login == senha:
    print('Entrou')
elif entrada == 'E' and login != senha:
    print('Senha incorreta')
else:
    print('Sair')


