print('Calcule a distância entre 2 pontos no plano!')
print('____')

print('Informe as coordenadas de x1 e y1.')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
print('____')

print('Informe as coordenadas de x2 e y2.')
x2 = float(input('x2: '))
y2 = float(input('y2: '))
print('__________')

dist = int(((x2 - x1) * 2) + ((y2 - y1) * 2))
aprox = round(float(dist ** 0.5), 2)

print(f'A distância entre os 2 pontos é √{dist} !')
print('__________')
print(f'--> Dessa forma, o valor exato ou aproximado da distância é {aprox} !')
