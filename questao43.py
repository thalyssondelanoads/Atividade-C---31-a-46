print('Calcular X e Y em uma sistema de equação linear')
print('---------------')

print('Digite o valor dos coeficientes:')
a = int(input(' a = '))
b = int(input(' b = '))
c = int(input(' c = '))
d = int(input(' d = '))
e = int(input(' e = '))
f = int(input(' f = '))

r1 = (c * e - b * f)/(a * e - b * d )
r2 = (a * f - c * d)/(a * e - b * d )
x = round(r1,2)
y = round(r2,2)

print('------------')
print(f' O valor de X é {x}.')
print(f' O valor de Y é {y}.')
