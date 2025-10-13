'''
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

'''
distancia_em_km = int(input("Digite a distancia percorrida em kilometros: "))

if distancia_em_km < 100:
    print("O valor do pedágio será: 10.00")
elif 100 < distancia_em_km < 200:
    print("O valor do pedágio será: 20.00")
elif distancia_em_km > 200:
    print("O valor será 30.00") 