"""
WHILE: adivinhar um numero entre 1 e 100
"""
import random
num = random.randrange(1, 101)  #numero entre 1 e 100

palpites = 1
upalpite = int(input("Adivinhe um numero entre 1 e 100. \n"))

while upalpite != num:
    palpites = palpites + 1
    if upalpite > num:
        print(upalpite, "esta acima.")
    elif upalpite < num:
        print(upalpite, "esta abaixo.")
    upalpite = int(input("Tente novamente: \n"))
print("Otimo, voce acertou em" , palpites , "tentativas!")