valor = int(input('Digite o valor da compra:'))
vip = input('Você é vip ? ').lower()

if valor >= 100 and vip == "sim":
    desconto = valor * 0.20
    final = valor - desconto
    print(f'Voce recebeu 20% de desconto')
    print(f'valor final {final}')
elif valor >= 100 or vip == "sim":
    desconto = valor * 0.10
    final = valor - desconto
    print(f'Voce recebeu 10% de desconto')
    print(f'Valor final {final}')
else:        
    print('Sem desconto')