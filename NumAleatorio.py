from random import randint
x = randint(0, 10)

resposta = int(input("De 0 a 10 escolhe um numero: "))

if resposta == x:
    print("Acertaste")
else:
    print("Erraste")