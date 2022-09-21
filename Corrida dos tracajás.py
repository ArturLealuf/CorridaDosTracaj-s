tam = int(input('qual o tamanho do grupo de tracajás: '))
while tam > 50 or tam < 1:
    print('numero invalido. valor maximo = 50')
    tam = int(input('qual o tamanho do grupo de tracajás: '))
maior = 0
for i in range(tam):
    vel = int(input(f'Qual a velocidade media (em km/h) do tracajá {i+1}: '))
    while vel > 25 or vel < 1:
        print('numero invalido. velocidade maxima = 25')
        vel = int(input('qual o tamanho do grupo de tracajás: '))
if vel > maior:
    maior = vel 
nivel = 0
if maior < 10: nivel = 1 
elif maior < 15: nivel = 2
else: nivel = 3
print(f'o tracajá mais rapido deste grupo está no nivel {nivel}, com a velocidade: {maior}')