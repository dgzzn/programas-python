votos = []

print(5*'- '+'ENQUETE'+5*' -')
i = 1

while i != 0:
     i = int(input('Digite o número do jogador (0 = Encerrar programa): '))
     
     if i <= 23 and i > 0:
         votos.append(i)

melhor = 0

for i in range(1, 24):
    print('%i - %i'%(i, votos.count(i)))
    if melhor < votos.count(i):
        melhor = i
#print('Melhor = %i'%melhor)

print('VOTAÇÃO ENCERRADA')
print('JOGADOR DA PARTIDA: Camisa %i'%melhor)
print('Total de votos: %i'%(len(votos)))
for i in range(1, 24):
     print('Jogador %i: %i votos (%.2f%%)'%(i, votos.count(i), (100*votos.count(i)/len(votos))))
