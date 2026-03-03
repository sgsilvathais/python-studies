nome = input('Qual seu nome? ')  # input sempre retorna string, mesmo que o usuário digite um número, ele será tratado como texto

print(f'Seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

numero_1 = int(input('Digite um número: '))  # aqui o valor digitado pelo usuário é convertido para inteiro usando a função int(), o que permite realizar operações matemáticas com ele
numero_2 = int(input('Digite outro número: '))  # porém, se o usuário digitar algo que não pode ser convertido para inteiro, como "abc", o programa irá gerar um erro. Para evitar isso, podemos usar um bloco try-except para tratar a exceção:

print(f'A soma dos números é: {numero_1 + numero_2}')  # aqui o resultado será a concatenação das strings, pois input sempre retorna string
print(f'A soma dos números é: {int(numero_1) + int(numero_2)}')  # aqui o resultado será a soma dos dois números, pois eles são convertidos para inteiros antes da operação