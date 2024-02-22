print('Soma de Frações')
print('----------')

numerador1 = int(input('Digite o numerador da primeira fração : '))
denominador1 = int(input('Digite o denominador da primeira fração : '))
print('----------')

numerador2 = int(input('Digite o numerador da segunda fração : '))
denominador2 = int(input('Digite o denominador da segunda fração : '))

numerador_soma = numerador1 * denominador2 + numerador2 * denominador1
denominador_soma = denominador1 * denominador2

print('----------')
print(f'A soma das frações é : {numerador_soma}/{denominador_soma}')
