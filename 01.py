"""
Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno
e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com nota Máxima!", se a média for igual a dez.

"""

n1 = int(input("1 bimestre: "))
n2 = int(input("2 bimestre: "))
n3 = int(input("3 bimestre: "))
n4 = int(input("4 bimestre: "))
media = (n1 + n2 + n3 + n4) / 4


if media == 10:
    print("Aprovado com nota maxima!")

elif media >=7:
    print("Aprovado!")

else:
    print("Reprovado!")