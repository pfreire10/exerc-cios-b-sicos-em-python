a = input("Digite o primiro número inteiro: ")
b = input("Digite o segundo número inteiro: ")
c = input("Digite o terceiro número inteiro: ")

n1 = int(a)
n2 = int(b)
n3 = int(c)

if a >= b and a >= c:
    print(f'O maior número é: {a}')
elif b >= a and b >= c:
    print(f'O maior número é: {b}')
else:
    print(f'O maior número é: {c}')

if a <= b and a <= c:
    print(f'O menor número é: {a}')
elif b <= a and b <= c:
    print(f'O menor número é: {b}')
else:
    print(f'O menor número é: {c}')

if a == b and a == c:
    print('Todos os números são iguais.')
elif a == b:
    print(f'O primeiro e o segundo números são iguais: {a}. O terceiro é diferente: {c}.')
elif a == c:
    print(f'O primeiro e o terceiro números são iguais: {a}. O segundo é diferente: {b}.')
elif b == c:
    print(f'O segundo e o terceiro números são iguais: {b}. O primeiro é diferente: {a}.')
else:
    print('Todos os números são diferentes.')