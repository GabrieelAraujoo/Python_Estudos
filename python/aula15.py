senha = '123'
login = input('Digite sua senha: ')
entrada = input('[E]ntrar [S]air: ')

if (entrada == 'E' or entrada == 'e') and login == senha:
    print('Entrou')
elif (entrada == 'E' or entrada == 'e') and login != senha:
    print('Senha incorreta')
else:
    print('Sair')
