print('Calcular custo de um veículo')
print('-----')
print('DADOS : Impostos = 45%')
print('Porcentagem do Distribuidor = 28%')
print('-----')

custo_fab = float(input('Qual o custo de fabrica do veículo? : '))

imposto = custo_fab * 9/20
porcent = custo_fab * 14/50
custo_final = int(imposto + porcent + custo_fab)

print('----')
print(f'Seu Veículo irá custar {custo_final} Reais !')
