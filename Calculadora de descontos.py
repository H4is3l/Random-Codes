print(' ==Calculadora de Porcentagem== ')

b = float ( input ('Preço do produto: '))
b1 = float (input('Porcentagem de desconto: '))
    
d = float (b1 / 100)
d1 = float  (d * b)
d2 = float (b - d1)
    
print(f'O desconto será de {d1:.2f}, resultando no total de: {d2:.2f}')

    