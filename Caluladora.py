#Variaveis.
vCartao = float(input('Quanto dinheiro há no seu cartão :'))
vPassagem = float(input('Quanto custa uma passagem :'))
dUso = float(input('Quantos vezes em um dia você utiliza este meio de transporte :'))
#Calculo de quantas passagens é possível utilizar.
print('O total de passagens que podem ser utilizadas é de {:.2f} .'.format(vCartao / (vPassagem * dUso)))
