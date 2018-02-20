# Somar os n primeiros números do "num"
# Ex. 
#   3 -> 1+2+3 = 5
#   4 -> 1+2+3+4 = 10
#   5 -> 1+2+3+4+5 = 15
#   6 -> 1+2+3+4+5+6 = 21

# Início
num = int(input("Digite um número: "))

soma = 0
cont = 1

while cont <= num:
    soma = soma + cont
    cont += 1

print("A soma dos números de 1 até",num,"é =",soma)
