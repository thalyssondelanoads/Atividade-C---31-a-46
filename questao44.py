print('Calcular a quantidade de Cobre e Zinco necessárias para um latão')
print('------')

kg = float(input('Quantos Quilogramas? : '))

cobre = int(kg * 0.7)
zinco = int(kg * 0.3)

print('-----')
print('Serão necessárias as seguintes quantidades de cada componente: ')
print(f'--> Cobre ≈ {cobre} Kg')
print(f'--> Zinco ≈ {zinco} Kg')
