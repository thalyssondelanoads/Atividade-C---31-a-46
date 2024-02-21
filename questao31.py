print('Converter um número de 4 dígitos binários para a base decimal')
print('-----------')

num_bin = int(input('Digite o número binário: '))

num_1 = num_bin // 1000
num_2 = num_bin % 1000 // 100
num_3 = num_bin % 100 // 10
num_4 = num_bin % 10
resultado = (num_1 * 2**3) + (num_2 * 2**2) + (num_3 * 2**1) + (num_4 * 2**0)

print('------------')
print(f'O número na base decimal é {resultado}')
