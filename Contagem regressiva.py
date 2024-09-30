import pygame

#Entrada:
print('Iniciando processso de contagem regressiva!')
n = str(input('Digite "sim" para começar a contagem regressiva: ')).lower()

#Processamento e Saída:

if n in ('sim','Sim','yes','Yes','y','Y','s','S','si','Si'):
    pygame.init()
    pygame.mixer.music.load('CTG.mp3')
    pygame.mixer.music.play()
    
    pygame.mixer.music.queue('meme.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

print('Contagem finalizada!')
