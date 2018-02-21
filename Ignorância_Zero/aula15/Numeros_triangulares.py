"""
Dizemos que um número natural é triangular se ele é produto de três números
naturais e consecutivos.

Exemplo: 120 é triangular, pois 4x5x6 == 120.

Dado um inteiro não-negativo n, verificar se n é triangular.

num = int(input("Digite um número: "))

# Variáveis que irão ser incrementadas para serem usadas na multiplicação
i, j, k = 1, 2, 3

while i * j * k < num:
    i += 1
    j += 1
    k += 1
if i * j * k != num:
    print(num,"Não é triangular")
else:
    print(num,"é triangular, pois a multiplicação dos números",i,"x",j,"x",k,"é =",num)

Ou o programa pode ser escrito sem precisar de 03 variáveis, podendo ser usado apenas 01 
variável e sendo incrementada.
"""

num = int(input("Digite um número: "))
i = 1

while i * (i + 1) * (i + 2) < num:
    i += 1

if i * (i + 1) * (i + 2) == num:
    print(num,"é triangular")
else:
    print(num,"Não é triangular")