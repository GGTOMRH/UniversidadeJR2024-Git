from random import randint
perguntas = 0
acertaste = 0
numeroDeperguntas = 815


while perguntas < numeroDeperguntas:

    numero1 = randint(1, 10)
    numero2 = randint(1, 10)
    operador = randint(1, 4)

    if operador == 1:
        resposta = input(str(numero1) + " + " + str(numero2) + " = ?: ")
        if float(resposta) == numero1 + numero2:
            print("Acertaste")
            acertaste += 1
        else:
            print("Erraste")
    elif operador == 2:
        resposta = input(str(numero1) + " - " + str(numero2) + " = ?: ")
        if float(resposta) == numero1 - numero2:
            print("Acertaste")
            acertaste += 1
        else:
            print("Erraste")
    elif operador == 3:
        resposta = input(str(numero1) + " * " + str(numero2) + " = ?: ")
        if float(resposta) == numero1 * numero2:
            print("Acertaste")
            acertaste += 1
        else:
            print("Erraste")
    else:
        resposta = input(str(numero1) + " / " + str(numero2) + " = ?: ")
        if float(resposta) == numero1 / numero2:
            print("Acertaste")
            acertaste += 1
        else:
            print("Erraste")
    perguntas += 1
print("Tu acertaste " + str(acertaste) + " de " + str(numeroDeperguntas) + " perguntas!")