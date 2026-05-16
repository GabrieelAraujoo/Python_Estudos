"""
Repetições 
while (enquanto)
executa uma ação quando uma condição for verdadeira 
loop infinito - > Quando um codigo n tem fim

"""

contador = 0 

while contador < 100:
    contador += 1 

    if contador == 6:
        continue

    if  contador >= 20 and contador <= 35:
        print('não quero mostrar os 15 numeros') 
        continue 

    print(contador)

    if contador == 90: 
        break
        

print('Acabou')
