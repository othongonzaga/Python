preço = float(input('Qual o preço do produto? R$'))
pagamento = input('O pagamento vai ser à vista? ')
pagVista = preço - (preço * 10/100)
pagParcelado = preço + (preço * 8/100)

if pagamento == 's':
    print('O valor final do produto é: R${:.2f}'.format(pagVista))
else:
    print('O valor final do produto é: R${:.2f}'.format(pagParcelado))    