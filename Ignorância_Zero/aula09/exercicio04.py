"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 4 litros,
que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga no tamanho da area e sempre arredonde os valores para cima,
isto é, considere latas cheias.
"""
area = int(input("Qual o tamanho da área a ser pintada? "))
print("Area digitada foi: ",area)
# Acrescentando 10% no tamanho da área
area = area*1.1
print("Area acrescida de 10% é: ",area)


# Calular o quanto excedeu no valor da área
excesso = area - int(area)
area = int(area)

if excesso > 0:
    area = area + 1
"""
# Divisão inteira
litros = area//6

if area % 6 > 0:
    litros = litros + 1
     
latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

galoes = litros//4
if litros % 4 > 0:
    galoes = galoes + 1

print("Você precisa de",litros,"litros para cobrir a área informada")
if litros >= 4:
    print("Você precisa de",litros,"litros para cobrir a área informada")
    print("Você irá precisar de",galoes,"galoes para pintar")
    print("Valor pago nos galoes será R$",galoes*25)
    if litros >= 18:
        print("Ou você pode comprar",latas,"latas para pintar")
        print("Valor pago nas latas será R$",latas*25)
"""