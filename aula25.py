"""
is, is not e None


Variável é tipo uma caixa.

nome = 'Gabriel' --- > A caixa nome tem: Gabriel

E o None?

nome = None

Significa: a caixa existe MAS ela tá vazia

nome = None --- > nome: (vazio)

O is None

Serve pra perguntar: essa variável tá vazia?

nome = None

"""
if nome is None: # type: ignore
    print('A variável está vazia')

#############################################################################

nome = 'Gabriel'

if nome is None:
    print('Está vazio')
else:
    print('Tem valor')

# Porque agora a caixa NÃO está vazia.

"""
is not

É o contrário: não é isso?

"""
nome = 'Gabriel'

if nome is not None:
    print('Tem nome')

"""
FLAG 

Flag é só uma variável usada pra marcar algo.

Tipo um interruptor:

ligado
desligado

logado = False 
Significa: usuário não está logado

logado = True
usuário está logado

"""

senha = '1234'
acesso = input('Digite a senha: ')

logado = False

if acesso == senha:
    logado = True

if logado:
    print('Entrou')
else:
    print('Senha incorreta')



