'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C.
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

'''
temperatura_atual = int(input("Digite a temperatura atual do local: "))

if temperatura_atual > 25:
    print("ALERTA! A temperatura está muito alta.")
else:
    print("A temperatura está adequada.")