print('Critério da Distribuição Ótima')
print('----------')

valor = int(input('Qual valor deseja sacar? : '))

nota_cinq = valor // 50
novo_valor1 = valor - (nota_cinq * 50)
nota_dez = novo_valor1 // 10
novo_valor2 = novo_valor1 - (nota_dez * 10)
nota_cinco = novo_valor2 // 5 
novo_valor3 = novo_valor2 - (nota_cinco * 5)
nota_um = novo_valor3

print('----------')
print('Você irá receber :')
print(f'--> {nota_cinq} Nota(s) de 50')
print(f'--> {nota_dez} Nota(s) de 10')
print(f'--> {nota_cinco} Nota(s) de 5')
print(f'--> {nota_um} Nota(s) de 1')
