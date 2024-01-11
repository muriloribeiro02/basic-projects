km = float(input('Quantos km por hora o carro passou? '))

if km > 80:
    print('Você foi multado!!')
multa = (km-80) * 7
print('Você deve pagar R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança')