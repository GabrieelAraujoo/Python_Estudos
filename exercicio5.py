nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

if idade < 18:
    print('Acesso permitido')
elif nome == "admin" and idade >= 18 .lower(): 
    print('Acesso especial concedido')
else:
    print('Acesso negado')

