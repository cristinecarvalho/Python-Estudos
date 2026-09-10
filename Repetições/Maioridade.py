from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nasc = int(input("Em que ano a pessoa nasceu?: "))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas de maior'.format(maior))
print('Ao todo tivemos {} pessoas de menor'.format(menor))