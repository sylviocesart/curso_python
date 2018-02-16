"""
Complementando as estruturas de decisao
Aqui iremos aprender o if, elif e else

Faça um programa que leia um número e exiba o dia correspondente da semana.
Ex:
    1-Domingo
    2-Segunda
    3-Terça, etc

Caso digite outro valor, deve aparecer "valor inválido"

"""
num = int(input("Digite um número: "))

if 1 <= num <= 7:
    if num == 1:
        print("Domingo")
    elif num == 2:
        print("Segunda-feira")
    elif num == 3:
        print("Terça-feira")
    elif num == 4:
        print("Quarta-feira")
    elif num == 5:
        print("Quinta-feira")
    elif num == 6:
        print("Sexta-feira")
else:
    print("Número inválido")
