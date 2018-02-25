"""
Vamos fazer uma série de exercíos para fixação do conteúdo 
que foi exposto até aqui.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Exercício:
Dizemos que um número natural é palíndromo se o 1º algarismo for igual
ao último, o 2º algarismo for igual ao penúltimo, e assim por diante
Exemplo:
567765 e 32423 são políndromos
567675 não é políndrom

Dado um número natual n > 10, verificar se n é políndromo.
"""
n = input("Digite um número: ")

if n == n[::-1]:
    print("Número %s é políndromo" %(n))
else:
    print("Não é políndromo")