"""
Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
"""
 
n1 = 40
n2 = 50
n3 = 10

maior = n1
if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3

menor = n1
if n2 < menor:
    menor = n2

if n3 < menor:
    menor = n3

print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")