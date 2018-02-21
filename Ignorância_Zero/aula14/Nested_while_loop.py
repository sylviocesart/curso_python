"""
Aqui vamos mostrar um exemplo de quando usar um while dentro
de outro while

Normalmente usa um while dentro de outro quando a execução de uma
variável está ligada à outra variável.
"""
i = 0
j = 0
n = 5

while i < n:
    while j < n:
        print(j)
        j += 1
    print(i)
    i += 1