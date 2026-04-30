"""
Exercício: Sistema de login com bloqueio
Você vai simular um sistema de autenticação simples.

:pushpin: O programa deve pedir:

Usuário
Senha


:brain: Regras:
:closed_lock_with_key: Credenciais corretas:

Usuário: admin
Senha: 1234


:rotating_light: Lógica do sistema:
1. Se usuário e senha estiverem corretos
 "Login realizado com sucesso"
2. Se usuário estiver correto mas senha errada
 "Senha incorreta"
3. Se usuário estiver errado
 "Usuário não encontrado"

:fire: Desafio extra (importante)
Adicionar:

Perguntar quantas tentativas o usuário já fez (número)
Se tentativas ≥ 3:
"Conta bloqueada"
:point_right: Essa condição deve ser verificada antes de tudo

:outbox_tray: Saída esperada (exemplos):

Login realizado com sucesso
Senha incorreta
Usuário não encontrado
Conta bloqueada


:warning: Regras obrigatórias:

Usar if, elif, else
Usar and
Tratar entradas com .lower() (para usuário)


:bulb: Dica estratégica (não é resposta)
A ordem das condições importa MUITO:
:point_right: Primeiro verifica bloqueio
 :point_right: Depois valida login

"""
usuario = 'admin'
senha = 1234
tentativas = 0

nome = input('Usuario: ')

if nome == usuario:
    while tentativas < 3:
        acesso = int(input('Senha: '))

        if acesso == senha:
            print('login realizado com sucesso')
            break
        else:
            print('senha incorreta')
            tentativas += 1
    print('seu acesso foi bloqueado')      
else:
    print('Usuario não encontrado')
