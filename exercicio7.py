nome = input('Digite seu nome: ').strip().lower()
idade = int(input('Digite sua idade:'))
salario = int(input('Digite seu salário:')) 

if idade >= 18 and salario >= 2000:
    print('Cadastro aprovado')
elif idade >= 18 and salario < 2000:
    print('Cadastro aprovado com restrições')
else:
    print('Cadastro negado') 


if nome == "admin":
    print('Usuário administrador detectado')

    