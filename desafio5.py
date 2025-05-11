#Faça um programa para ver a tabuada
n = int(input('digite um numero para ver a tabuada: '))
for i in range (1,15):
    resultado = i * n
    print(f'{i:2} x {n} = {resultado:3}')