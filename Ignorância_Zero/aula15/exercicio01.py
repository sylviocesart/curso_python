"""
Dizemos que um inteiro positivo n é perfeito se for
igual a soma de seus divisores positivos diferentes
de n.

Exemplo: 6 é perfeito, pois 1+2+3 = 6

Dado um inteiro positivo n, verificar se n é perfeito
"""
n = int(input("Digite um número: "))

cont, soma = 2, 1

while cont < n:
    if n % cont == 0:
        print(cont)
        soma += cont
        print(soma)
    cont += 1
if soma == n:
    print("O número",n,"é perfeito")
else:
    print("O número",n,"não é perfeito")