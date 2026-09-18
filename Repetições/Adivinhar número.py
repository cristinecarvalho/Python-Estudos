from random import randint
comp = randint(0,10)
print('Acabei de pensar em um numero entre 0 e 10')
print('Adivinhe qual: ')
acerto = False #Ainda não acertou, recebe false
palpite = 0 #Contador começa em zero
while not acerto: #Enquanto não acertou, repita, e se not false vira true, while começa
    jogador = int(input('Digite um numero entre 0 e 10: '))
    palpite += 1 #Cada tentativa aumenta o contador
    if jogador == comp:
        acerto = True #Se o jogador acertar, vira true
    else:
        if jogador < comp: #Se errar e o número digitado for maior
            print('Mais... Tente novamente')
        elif jogador > comp: #Se errar e o número digitado for menor
            print('Menos... Tente novamente')
print('Acertou com {} tentativas.'.format(palpite))