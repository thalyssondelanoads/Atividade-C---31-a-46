print('Simular Entrada e Parcelas')
print('----------')

valor_mercadoria = float(input('Qual o valor da mercadoria? '))

entrada = valor_mercadoria // 3
prestacao = (valor_mercadoria - entrada) // 2
prestacao += valor_mercadoria - (entrada + 2 * prestacao)
entrada += prestacao % 2

print('----------')
print(f'Entrada: R${entrada:.2f}, Prestações (2x): R${prestacao:.2f}')
