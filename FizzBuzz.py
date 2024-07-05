numero = 1

while numero <= 100:
        if numero%3 == 0 and numero%5 == 0:
                print("FizzBuzz")
                numero += 1
                continue
        if numero%3 == 0:
                print("Fizz")
                numero += 1
                continue
        if numero%5 == 0:
                print("Buzz")
                numero += 1
                continue
        
        else:
                print(numero)
                numero += 1
