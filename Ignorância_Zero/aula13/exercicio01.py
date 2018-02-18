"""
Faça um programa que peça dois números, base e expoente, calcule
e mostre o primeiro número elevado ao segundo número.

Não utilize a função potência da linguagem.
2**3 = 1*2*2*2 = 8
2**4 = 1*2*2*2*2 = 16


# Início do programa
base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor expoente: "))

# O número do expoente indica o número de vezes que a base
# será multiplicada.

cont = 0
produto = 1

while cont < expoente:
    produto *= base
    cont += 1

print(base,"elevado a",expoente,"=",produto)

# Fim

Usando a função potência, ficaria assim:
"""

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor expoente: "))

print(base,"elevado a",expoente,"=",base**expoente)