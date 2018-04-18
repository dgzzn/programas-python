"""
Escreva um programa que recebe uma lista de números até que seja dada 
a entrada -1, e depois imprima todos os números pares da sequência.
"""

numeros = []
pares = []

while True:
    x = int(input('Digite um número: '))
    if x != -1:
        numeros.append(x)
    else:
        break

for i in numeros:
    if i % 2 == 0:
        pares.append(i)

print('Números pares: ')
print(pares)