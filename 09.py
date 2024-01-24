"""
FOR: aumentar e diminuir, printar o maximo q o usuario quer.
"""

for c in range(1, 6):
    print(c)
print("Starting game!")

print("\n")

for c in range(5, 0, -1):
    print(c)
print("Starting game!")

num = int(input("Digite um numero: "))
for x in range(0 , num + 1):
    print(x)
print("FIM")