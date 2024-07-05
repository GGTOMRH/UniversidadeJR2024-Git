numero = input("Diz me um numero: ")
resposta = 1
numini = numero
numero = int(numero)

while numero > 1:
    resposta = resposta * numero
    numero -= 1

print("O factorial de " + numini + " é " + str(resposta))