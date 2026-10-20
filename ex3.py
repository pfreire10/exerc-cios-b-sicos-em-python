n1 = input('Digite a primeira nota: ')
n2 = input('Digite a segunda nota: ')

n1 = float(n1)
n2 = float(n2)

media = (n1 + n2) / 2

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
    print('Nota inválida.')
elif media >= 7:
    print('Aprovado!')
elif media >= 5 and media < 7:
    print('Recuperação!')
else:
    print('Reprovado!')
