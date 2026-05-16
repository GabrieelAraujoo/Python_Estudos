"""
operadores de atribuição 

= += -= *= /= //= **= %=

Aqui está um resumo rápido dos três operadores que costumam gerar dúvida:

//= — divisão inteira (descarta a parte decimal): 10 // 3 → 3
**= — potenciação: 10 ** 2 → 100
%= — módulo, ou seja, o resto da divisão: 10 % 3 → 1

Os demais (+=, -=, *=, /=) são apenas atalhos para escrever 
x = x + n, x = x - n, etc. — bem convenientes no dia a dia.

"""

contador = 0 

while contador <= 10:
    contador += 1
    print(contador )
          
print("acabou")       