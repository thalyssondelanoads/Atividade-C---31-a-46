print('Calcular a expressão D = (R + S)/2')
print('Onde R = (A+B)*2 | S = (B + C)*2')
print('--------')

a = int(input('Digite o valor de A : '))
b = int(input('Digite o valor de B : '))
c = int(input('Digite o valor de C : '))

r = (a + b)**2
s = (b + c)**2
d = int((r + s)/2)

print('---------')
print(f'O resultado da expressão é {d} !')
