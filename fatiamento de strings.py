"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
    i - início
    f - fim
    p - passo
Obs.: a função len retorna a quantidade de caracteres da string, incluindo espaços
"""

variavel = 'Olá mundo'
print(variavel[0:8:])  # aqui estamos fatiando a string do índice 0 até o índice 7 (o índice 8 não é incluído), o que resulta na string 'Olá mund'
print(len(variavel))  # aqui estamos usando a função len para obter a quantidade de caracteres da string, que é 9, incluindo o espaço
print(variavel[-1:-10:-1])