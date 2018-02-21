"""
Dado um número inteiro positivo n, imprimir os n primeiros
naturais ímpares.
Exemplo:
    n = 4 --> 1, 3, 5, 7
    n = 3 --> 1, 3, 5
    n = 7 --> 1, 3, 5, 7, 9, 11, 13
"""
n = int(input("Quantos números primos você quer visualizar? "))
aux = n
cont = 1

while cont <= n:
    n = n + 1
    print(cont)
    cont += 2