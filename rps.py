from random import randint
x = randint(1, 3)

resposta = input("Pedra, Papel ou Tesoura?: ")

if resposta == "pedra" and x == 1:
    print("Empate")
elif resposta == "pedra" and x == 2:
    print("Perdeste")
elif resposta == "pedra" and x == 3:
    print("Ganhaste")
elif resposta == "papel" and x == 1:
    print("Ganhaste")
elif resposta == "papel" and x == 2:
    print("Empate")
elif resposta == "papel" and x == 3:
    print("Perdeste")
elif resposta == "tesoura" and x == 1:
    print("Perdeste")
elif resposta == "tesoura" and x == 2:
    print("Ganhaste")
elif resposta == "tesoura" and x == 3:
    print("Empate")