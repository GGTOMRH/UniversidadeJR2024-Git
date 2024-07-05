from random import randint
x = randint(0, 1000)
resposta = int(input("Diz me um numero de 0 a 1000: "))

while x != resposta:
    if x < resposta:
        resposta = int(input("O numero é menor.Tenta denovo: "))
    elif x > resposta:
        resposta = int(input("O numero é maior.Tenta denovo: "))

print("Acertaste!")