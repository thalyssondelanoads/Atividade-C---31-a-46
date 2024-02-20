print('Calcular dinheiro gasto com cigarros ao longo da vida')
print('--------')

ano = int(input('A quantos anos vc fuma? : '))
num_cig = int(input('Quantos cigarros vc fuma por dia? : '))
preço = float(input('Qual o preço da carteira de cigarro? : '))

dia = ano * 365
carteira = num_cig / 20 
valor = dia * carteira * preço

print('---------')
print(f'Você gastou {valor} Reais com cigarro ao longo de sua vida! ')
