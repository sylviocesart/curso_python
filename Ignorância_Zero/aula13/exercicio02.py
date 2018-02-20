"""
Dado um número inteiro não negativo n, determinar n!
Exemplo:
    5! = 5*4*3*2*1
    3! = 3*2*1

# Usando exemplo decrementando:
# Início
num = int(input("Digite um número: "))

# Vamos supor que num=4, cont seria cont=4-1, ou seja, cont=3
cont = num - 1

# Será uma variável auxiliar que ficará sendo decrementada em 1
produto = num

while cont > 1:
    # 4 = 4 * 3
    produto = produto * cont

    # cont = 4 - 1, cont=3
    cont -= 1

print(num,"! =",produto)

# Fim

Usando incrementando
"""
# Início
num = int(input("Digite um número: "))

produto = 1
cont = 2

while cont <= num:
    produto = produto * cont
    cont += 1

print(num,"! =",produto)