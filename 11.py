"""
FOR: pedir um valor n vezes e somar
"""
s = 0
for x in range (0, 3):
    n = int(input("Digite um valor: "))
    s = s + n
print("O resultado da soma foi: " , s)