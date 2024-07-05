numero1 = float(input("Primeiro numero: "))
operador = input("Qual operador: ")
numero2 = float(input("Segundo numero: "))

if operador == "+":
    print(numero1 + numero2)
elif operador == "-":
    print(numero1 - numero2)
elif operador == "*":
    print(numero1 * numero2)
else:
    print(numero1 / numero2)