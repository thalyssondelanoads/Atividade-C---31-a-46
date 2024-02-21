print('Transformar Dias em Anos, Meses e Dias')
print('-----------')

idade_dias = int(input('Digite a idade em dias: '))

ano = idade_dias // 365
mes = (idade_dias % 365) // 30
dia = (idade_dias % 365) % 30

print('-----------')
print(f'A idade é {ano} anos, {mes} meses e {dia} dias')
