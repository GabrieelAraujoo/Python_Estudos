"""
imtaveis que vimos: str, int, float, bool 

"""

string = '1000'
outra_variavel = f'{string[:3]}ABC{string[4:]}' # ele fatia a string em dois
#  pedaços e enfia 'ABC' no meio, substituindo o caractere do índice 3 (h) que ficou de fora. 
# É uma forma de trocar parte de uma string por outro texto.

outra_variavel = f'{string[:3]}ABC{string[4:]}'
#                   'Pyt'  +  'ABC'  +  'on'
#                        = 'PytABCon'

# print(string)
# print(outra_variavel)
print(string.zfill(10))

