salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 15/100)

print('Com o aumento, o novo salario do funcionário é: R${:.2f}'.format(novo))