"""Exercicios Básicos Python
Aldo Evan"""
# Execicio 1

num = int(input('Digite um numero: '))
print("o numero digitado foi:", num)
print(type(num))

# Exercicio 2

nume = float(input('Digite um numero real: '))
print(f'O numero digitado foi: {nume}')
print(type(nume))

# Exercicio 3

print("Digite 3 numeros")
a = int(input(f'digite o primeiro numero:'))
b = int(input(f'digite o segundo numero:'))
c = int(input(f'digite o terceiro numero'))

soma = a + b + c
print(f'O resultado da soma dos 3 numeros é: {soma}')

# Exercicio 4

valor = float(input(f'Digite um numero:'))

quad = (valor**2)
print(f'O quadro desse numero é {quad}')

# Exercicio 5

valor = float(input(f'digite o numero:'))
div = valor/5
print(f'A quinta parte do numero é {div}')

# Exercicio 6

C = float(input("Digite o valor da temperatura em Celcius:"))

F = float(C*(9/5)+32)
print(f'O valor em Fahrenheit é :{F}')

# Exercicio 9

Ke = C + 273.15
print(f'O valor da temperatura em Kelvin: {Ke}')

# Exercicio 7

F = float(input('Digite o valor da temperatura em Fahrenheit'))
C = float(5*(F-32)/9)
print(f'O Valor em Celcius é: {C}')

# Exercicio 8

K = float(input(f'digite a temperatura em Kelvin:'))
Ce = float(K - 273.15)
print(f'O valor em celcius é:{Ce}')

# Exercicio 10
K = float(input('Digite a velocidade em Km/h: '))
M = float(K/3.6)
print(f'A velocidade em m/s é: {M}')
Inv = float(input('Digite a velocidade em m/s:'))
R = float(Inv*3.6)
print(f'O resultado em km/h é: {R}')