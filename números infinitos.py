import random

numero = 0
numero1 = 0

while numero >= 0:
    for i in range(1):

        num = random.random()*(10**10)
        numero = num

        num1 = random.random()*(10**10)
        numero1 = num1

        print(numero)
        print(numero1)

        if numero >= numero1:
            break
        
        if numero1 >= numero:
            break

        

