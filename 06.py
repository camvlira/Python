"""
Faca um programa que calcule as raizes de uma c
O programa devera pedir os valores de a, b e c e fazer as consistencias, informando ao usuario nas seguintes 
situacoes:

Se o usuario informar o valor igual a zero, a equacao nao eh do segundo grau e o programa nao deve pedir 
os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equacao nao possui raizes reais. Informe ao usuario e encerre o programa;
Se o delta calculado for igual a zero a equacao possui apenas uma raiz real; informe-a ao usuario;
Se o delta for positivo, a equacao possui duas raizes reais; informe-as ao usuario.
"""

a = int(input("Digite o valor de A: "))

if a == 0:
    print("Programa encerrado. Valor deve ser maior que 0.")
    exit()

else:
    b = int(input("Digite o valor de B: "))
    if b == 0:
        print("Programa encerrado. Valor deve ser maior que 0.")
        exit()
    else:
        c = int(input("Digite o valor de C: "))
    
if c == 0:
    print("Programa encerrado. Valor deve ser maior que 0.")
    exit()

"""
Delta = b'2 – 4ac
X = – b ± √Δ
    2·a
"""

delta = (b ** 2) - (4 * a * c)
x1 = (-b + (delta**(1/2))) / (2 * a)
x2 = (-b - (delta**(1/2))) / (2 * a)

print(f"Valor de delta: {delta}")
if delta < 0:
    print("Delta negativo, a equacao nao possui raizes reais. Programa encerrado.")

elif delta == 0:
    print(f"Delta igual a 0. Unica raiz real possivel: {x1 :.2f}" )

else:
    print(f"Raizes reais possiveis: {x1 :.2f} e {x2 :.2f}")