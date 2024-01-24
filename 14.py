"""
For: soma dos numeros impares e multiplos de 3 no intervalo de 1 a 500.
"""
x = 0
for n in range(1, 501, +2):
    if n % 3 == 0:
        x += n
print(x)