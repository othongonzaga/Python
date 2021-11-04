dias = int(input('Quantos dias vai alugar o automóvel? '))
km = float(input('Qauntos km você rodou? '))
pagar = (dias * 60) + (km * 0.15)

print('O preço final do aluguel é: R${}'.format(pagar))