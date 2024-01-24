"""
FOR: inicio, pular e fim
"""

i = int(input("Inicio: "))
p = int(input("Pular: "))
f = int(input("Fim:  "))

for x in range(i, f + 1, p):
    print(x)

