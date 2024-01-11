distancia = float(input('Qual será a distancia percorrida? '))
print('Voce esta prestes a começar a viagem de {} km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem será de {:.2f}'.format(preco))