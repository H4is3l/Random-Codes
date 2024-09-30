print('Calculadora de TMB')

s = input(' Você é Homem ou Mulher?')

p = float (input('Qual seu peso?'))

a = float (input ('Qual sua altura em cm?'))

i = float(input ('Qual sua idade?'))

c = float (66 + (13.7 * p) + (5 * a) - (6.8 * i))

c2 = float(665 + (9.6 * p) + (1.8 * a) - (4.7 * i))

if s == 'homem' or 'Homem':
    print(f'Seu metabolismo é: {c}!')
    
else:
    print(f'Seu metabolismo é: {c2}!')