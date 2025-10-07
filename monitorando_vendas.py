'''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado.
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas.
Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais.
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
Saída esperada:
'''
macas_vendidas = int(input(print("Digite a quantidade de maçãs vendidas: ")))
bananas_vendidas = int(input(print("Digite a quantidade de bananas vendidas: ")))

if macas_vendidas > bananas_vendidas:
    print("As maçãs foram a fruta mais vendida!")

elif macas_vendidas == bananas_vendidas:
    print("Houve um empate entre as frutas mais vendidas!")

else:
    print("As bananas foram a fruta mais vendida!")