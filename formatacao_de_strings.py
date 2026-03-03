"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f - float com número específico de casas decimais
x ou X - Hexadecimal
(Caracatere)(><^)(quantidade)(tipo - s, d, f, x, X)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r (repr), !s (str), !a (ascii)
"""
variavel = 'ABC'
print(f'{variavel}')  # aqui usamos a formatação de string moderna, onde f indica que é uma f-string e as chaves {} são usadas para inserir o valor da variável dentro da string
print(f'{variavel:>10}')  # aqui usamos o operador > para alinhar o texto à direita e o número 10 para definir a largura total da string, preenchendo com espaços à esquerda se necessário
print(f'{variavel:<10}')  # aqui usamos o operador < para alinhar o texto à esquerda e o número 10 para definir a largura total da string, preenchendo com espaços à direita se necessário
print(f'{variavel:^10}')  # aqui usamos o operador ^ para alinhar o texto ao centro e o número 10 para definir a largura total da string, preenchendo com espaços à esquerda e à direita se necessário
print(f'{variavel:*>10}')  # aqui usamos o operador > para alinhar o texto à direita, o número 10 para definir a largura total da string e o caractere * para preencher com asteriscos à esquerda se necessário
print(f'{1000.4873648123746:0>-10.1f}')