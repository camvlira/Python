print("Ola mundo!") 

#variaveis

inteiro = 0
teia = "Camily"
caractere = 'c'
quebrado = 3.5
decisao = False

lista = [10, "ola", True, 'R']
print(lista)
print(lista[1])

#operadores

"""
+
-
*
/
% modulo da divisao
// divisao com resultado inteiro
** potencia
"""

#Crie um programa que faca a soma, subtracao, multiplicacao e divisao de 2 numeros

x = 5
y = 5
print("\n",x + y,"\n",x - y,"\n",x * y,"\n",x / y,"\n")

nn1 = 5
nn2 = 5
print(f"A soma de {nn1} + {nn2} = {nn1 + nn2}")
print(f"A subtracao de {nn1} - {nn2} = {nn1 - nn2}")
print(f"A multiplicacao de {nn1} * {nn2} = {nn1 * nn2}")
print(f"A divisao de {nn1} / {nn2} =  {nn1 / nn2}")
print(f"A exponenciacao de {nn1} ** {nn2} = {nn1 ** nn2}")
print("\n")

#Operadores de atribuicao

"""
=   x =  1   x = 1
+=  x += 1   x = x + 1
-=  x -= 1   x = x - 1
*=  x *= 1   x = x * 1
/=  x /= 1   x = x / 1
%=  x %= 1   x = x % 1
"""

num1 = 10
num1 += 5
print(num1, "\n")


#Operadores de comparacao
"""

"""

#Nota final
"""
nota1 = 7
nota2 = 7
nota3 = 7
nota4 = 7

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aluno aprovado!")

else: 
    print("Aluno reprovado!")
"""


aluno = str(input("Digite o nome do aluno: "))
nota1 = int(input("1 bimestre: "))
nota2 = int(input("2 bimestre: "))
nota3 = int(input("3 bimestre: "))
nota4 = int(input("4 bimestre: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f"A media do aluno {aluno} foi {media} e com isso ele foi aprovado!")
    
else:
    print(f"A media do aluno {aluno} foi {media} e com isso ele foi reprovado!")
