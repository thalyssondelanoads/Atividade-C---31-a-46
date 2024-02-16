print('Converter idade para dias!')
print('-------')

ano = int(input('Quantos anos você tem? : '))
mes = int(input('Quantos meses ? : '))
dia = int(input('Quantos dias ? '))

dia1 = ano * 365
dia2 = mes * 12
dia3 = dia
dia_final = dia1 + dia2 + dia3

print(f' Você tem {dia_final} dias de vida! ')