print('Divisão segura!')
a = input('Digite o primeiro número: ')
b = input('Digite o segundo número: ')

a = float(a)
b = float(b)

if b == 0:
    print('Não é possível dividir por zero.')
else:
    resultado = a/b
    print(f'O resultado da divisão de {a} por {b} é: {resultado}.')