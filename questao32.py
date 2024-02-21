print('Diferença de um inteiro pelo seu inverso!')
print('------')

num = int(input('Qual o número? : '))

alg1 = num // 100
alg2 = num % 100 // 10 
alg3 = num % 10

resultado1 = (alg1 * 100) + (alg2 * 10) + (alg3)
resultado2 = (alg3 * 100) + (alg2 * 10) + (alg1)
resultado_final = resultado1 - resultado2

print('-------')
print(f'A diferença do número {num} com seu inverso é {resultado_final}!')
