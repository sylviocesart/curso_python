"""
Dada uma sequência de números inteiros não nulos,
finalize a lista em 0, imprimir quadrados.
"""
num = int(input("Digite o primeiro número: "))

while num != 0:
    print(num,"ao quadrado =",num*num)
    num = int(input("Digite o próximo número: "))

if num == 0:
    print("Valor nulo. Finalizando programa!!")