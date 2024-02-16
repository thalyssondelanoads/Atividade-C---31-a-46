print('Soma de elementos de um número inteiro de 4 dígitos')
print('------------')

numero = int(input(' Digite o número: '))

alg_1 = numero // 1000
alg_2 = numero % 1000 // 100
alg_3 = numero % 100 // 10
alg_4 = numero % 10
resultado = alg_1 + alg_2 + alg_3 + alg_4

print('------------')
print(f' Resultado = {resultado}')