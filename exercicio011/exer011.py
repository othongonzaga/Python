largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
pintura = area / 2

print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você vai precisar de {}L de tinta.'.format(pintura))