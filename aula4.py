fim = int(input('digite o valor final da sequencia:'))
contador = 0
print(f'sequencia de 0 até{fim}:')
for i in range (fim + 1):
    print(i)
    contador+= 1
print(f'quantidade de numeros gerados:{contador}')