#impar ou par:
loop = True
while loop:
    x = int(input('Insira um número: '))
    if x % 2 == 0:
        print('É par')
    else:
        print('É ímpar')
        loop = False