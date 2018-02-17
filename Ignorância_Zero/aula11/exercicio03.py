"""
Faça um programa que leia três números e mostre
o maior e o menor deles.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 == num2 == num3:
    print("Os números digitados sao iguais")
elif num1 >= num2 >= num3:
    print("O Maior número deles é:",num1,"e o menor é:",num3)
elif num1 >= num3 >= num2:
    print("O Maior número deles é:",num1,"e o menor é:",num2)
elif num2 >= num1 >= num3:
    print("O Maior número deles é:",num2,"e o menor é:",num3)
elif num2 >= num3 >= num1:
    print("O Maior número deles é:",num2,"e o menor é:",num1)
elif num3 >= num2 >= num1:
    print("O Maior número deles é:",num3,"e o menor é:",num1)
elif num3 >= num1 >= num2:
    print("O Maior número deles é:",num3,"e o menor é:",num2)