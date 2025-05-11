#Escreva um programa que peça três números inteiros ao usuário e exiba qual deles é o maior.
valor1 = int(input('Primeiro número: '))
valor2 = int(input('Segundo número: '))
valor3 = int(input('Terceiro número: '))
maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3
print('O maior valor é:', maior)