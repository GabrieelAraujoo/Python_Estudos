# Operador logico "not"
# Usado para inverter expressões
# not true = false 
# not false = true

senha = '123'
login = input('Digite sua senha: ')
entrada = input('[E]ntrar [S]air: ')

if (entrada == 'E' or entrada == 'e') and login == senha:
    print('Entrou')
elif not login == senha :
    print('Senha incorreta')
else:
    print('Sair')