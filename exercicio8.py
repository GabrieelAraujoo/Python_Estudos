numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))

# MAIOR NUMERO
if numero1 > numero2 and numero1 > numero3:
    print('Numero 1 é o maior numero')

elif numero2 > numero1 and numero2 > numero3:
    print('Numero 2 é o maior numero')

elif numero3 > numero1 and numero3 > numero2:
    print('Numero 3 é o maior numero')

else:
    print('Existe empate entre os numeros')


# MENOR NUMERO
if numero1 < numero2 and numero1 < numero3:
    print('Numero 1 é o menor numero')

elif numero2 < numero1 and numero2 < numero3:
    print('Numero 2 é o menor numero')

elif numero3 < numero1 and numero3 < numero2:
    print('Numero 3 é o menor numero')

else:
    print('Existe empate entre os numeros')


# TODOS IGUAIS
if numero1 == numero2 and numero1 == numero3:
    print('Numeros iguais')

    