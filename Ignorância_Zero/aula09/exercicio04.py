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
print("Area digitada foi:",area)

# Acrescentando 10% no tamanho da área
area = area*1.1
print("Area acrescida de 10% é:",area)

# Calular o quanto excedeu no valor da área
# Pegando as cadas decimais
excesso = area - int(area)
# Retirando a parte inteira da área
area = int(area)

if excesso > 0:
    # Arredondando para cima
    area += 1

# Calcular o número de litros para pintar a casa. Divisão inteira
litros = area//6
if area % 6 > 0:
    litros += 1

print("Litros necessários:",litros,"\n")

print("1) Comprar apenas latas de 18 litros")     
latas = litros//18
if litros % 18 > 0:
    latas += 1

print("Serão necessárias",latas,"latas")
print("Obteremos",latas*18,"litros")
print("Total: R$",latas*80)

print("\n2) Comprar apenas galões de 4 litros")
galoes = litros//4
if litros % 4 > 0:
    galoes += 1

print("Serão necessárias", galoes, "galoes")
print("Obteremos", galoes*4, "litros")
print("Total: R$", galoes*25)

"""
Vamos pensar, o preço total por litro pago nas latas é 80/18 ~ 4.44 R$/L
enquanto que para o gualão é 25/4 ~ 6.25 R$/L
portanto é sempre mais vantajoso comprar o máximo de latas possíveis
e o mínimo de galões, desde que o preço desses galoes não ultrapasse o preço
de uma lata, isto é, o numero de galoes seja menor ou igual a 3 (R$ 75)
"""
print("\n3)Misturar latas e galões, de forma que o preço seja o menor.")
latas = litros//18
galoes = 0
litros_restantes = litros%18

if litros_restantes <= 3*4:
    #Ou seja o numero de galoes necessarios seja menor do que três
    galoes = litros_restantes // 4
    if litros_restantes % 4 > 0:
        galoes += 1
else:
    latas += 1

print("Serão necessárias", latas, "latas")
print("Serão necessárias", galoes, "galoes")
print("Obteremos", latas*18 + galoes*4, "litros")
print("Total: R$", galoes*25 + latas*80)

"""
print("Você precisa de",litros,"litros para cobrir a área informada")
if litros >= 4:
    print("Você precisa de",litros,"litros para cobrir a área informada")
    print("Você irá precisar de",galoes,"galoes para pintar")
    print("Valor pago nos galoes será R$",galoes*25)
    if litros >= 18:
        print("Ou você pode comprar",latas,"latas para pintar")
        print("Valor pago nas latas será R$",latas*25)
"""