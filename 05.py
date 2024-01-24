"""
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

atual = float(input("Digite o salario atual: "))

if atual <= 280:
    reajuste = 20

elif atual <= 700:
    reajuste = 15

elif atual <= 1500:
    reajuste = 10

else:
    reajuste = 5

print(f"Salario antigo: {atual}")
print(f"Percentual de aumento: {reajuste}%")

reajuste_porc = reajuste / 100
aumento = atual * reajuste_porc
salario_novo = atual + aumento

print(f"Aumento: R$ {aumento}")
print(f"O novo salario sera: R${salario_novo}")