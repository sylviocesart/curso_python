"""
Dado um número inteiro positivo n,
Calcular a soma dos n primeiros números
inteiros positivos
Exemplo:
5 => 1+2+3+4+5 ou
5 => 5+4+3+2+1
"""
n = int(input("A sequência será de quantos númros? "))
cont = 0
soma = 0
while cont < n:
    num = int(input("Digite um número da sequência: "))
    if num > 0:
        soma = soma + num
    cont = cont + 1
print("Resultado:", soma)
"""

# Início
num = int(input("Digite um número: "))

soma = 1
cont = 2

while cont <= num:
    soma = soma + cont
    cont += 1

print("A soma dos números de 1 até",num,"é =",soma)
"""