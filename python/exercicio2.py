"""

Exercício: Sistema de acesso com múltiplas condições
Você vai criar um programa que simula um controle de acesso.
:pushpin: Regras:
O sistema deve pedir:

Nome do usuário
Idade
Se possui autorização especial (sim ou nao)

1. Se a pessoa tiver 18 anos ou mais
 Acesso liberado
2. Se tiver entre 16 e 17 anos
 Só entra se tiver autorização especial
3. Se tiver menos de 16 anos
 Acesso negado

"""

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
autorizacao = input('Você possui autorização:')

if idade >= 18:
    print('Acesso liberado')   
elif idade == 16 or idade == 17: 
    print('Só entra se tiver autorização especial')
    if autorizacao == "sim":
        print('Voce pode entrar')
    else:
        print('Voce não tem autorização')  
else:
    print('Acesso negado')    