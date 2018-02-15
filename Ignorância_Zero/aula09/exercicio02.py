"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamnho em metros quadrados da área
a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que
custam R$ 80,00.

Informe ao usuário a quantidade de latas de tinta a serem
compradas e o preço total.
"""
area = int(input("Qual o tamanho da área a ser pintada? "))

litros = area//3
if area % 3 >0:
    litros = litros + 1

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

valor = (latas*80)
print("Quantidade de litros:",litros)
print("Quantidade de latas",latas)
print("Quantidade de litros que temos com essas latas:",latas*18)
print("Valor a ser pago R$",valor)
