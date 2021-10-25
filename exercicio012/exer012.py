antes = float(input('Qual o preço do produto: R$'))
depois = antes - (antes * 5/100)

print('Com a promoção, o novo preço do produto é: R${:.2f}'.format(depois))