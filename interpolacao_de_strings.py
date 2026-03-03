"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""


nome = 'Thais'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)  # aqui usamos a formatação de string antiga, onde %s é um placeholder para string e %.2f é um placeholder para float com 2 casas decimais
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))  # aqui usamos o placeholder %d para inteiro e %08X para hexadecimal com 8 dígitos, preenchendo com zeros à esquerda se necessário