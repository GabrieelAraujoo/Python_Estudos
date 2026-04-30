
"""
Exercício: Validador de prioridade de incidentes (estilo NOC)
Você vai simular um sistema que classifica um incidente.

O programa deve pedir:

Nome do sistema
Tipo do problema (erro, alerta, info)
Se o sistema está fora do ar (sim ou nao)



:red_circle: PRIORIDADE CRÍTICA
Se:
• Tipo = erro
E
• Sistema está fora do ar = sim

:large_yellow_circle: PRIORIDADE MÉDIA
Se:
• Tipo = erro
OU
• Tipo = alerta

:large_green_circle: PRIORIDADE BAIXA
Se:

Tipo = info


:outbox_tray: Saída esperada:
Exemplo:

"Sistema X - PRIORIDADE CRÍTICA"
"Sistema Y - PRIORIDADE MÉDIA"
"Sistema Z - PRIORIDADE BAIXA"


:warning: Regras obrigatórias:

Usar if, elif, else
Usar operadores lógicos (and, or)
Usar .lower() nas entradas


:bulb: Dica importante (não é resposta)
A ordem das condições importa MUITO aqui.
:point_right: Se você errar a ordem, o programa classifica errado.

"""

nome_do_sistema = input('Digite o nome do sistema:')
tipo_do_problema = input('Digite o tipo do problema:').lower()
disponibilidade = input('O sistema esta fora do ar: ').lower()

if tipo_do_problema == "erro" and disponibilidade == "sim":
    print('Prioridade critica')
elif tipo_do_problema == "erro" or tipo_do_problema == "alerta":
    print('Prioridade média')
else:
    print('Prioridade baixa')        


