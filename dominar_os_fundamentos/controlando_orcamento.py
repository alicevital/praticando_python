'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos.
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas.
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

'''
despezas = float(input("Digite o valor gasto: "))

if despezas > 3000:
    print("O valor das despezas ultrapassou o limite")
elif despezas <= 3000:
    print("O valor está dentro do orçamento")