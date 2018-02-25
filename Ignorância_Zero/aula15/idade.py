"""
O outro atalho seria mais ou menos como
mostrado abaixo

n = int(input("Digite o número de pessoas: "))
cont = 0

while cont < n:
    dia = int(input("Digite o dia de nascimento: "))
    mes = int(input("Digite o mês de nascimento: "))
    ano = int(input("Digite o ano de nascimento: "))
    idade = int(input("Digite a idade a ser completada: "))

    print("A pessoa fará", idade, "anos no dia" , dia, "/", mes, "/", ano + idade)
    cont += 1

Agora, utilizando o segundo atalho, pois no exemplo acima, a saida foi:
dia / mes / ano
Perceba que existe um espaço entre o dia e o /
Vamos aprender como remover esse espaço
"""
n = int(input("Digite o número de pessoas: "))
cont = 0

while cont < n:

    dia = int(input("Digite o dia de nascimento da pessoa %i: "%(cont+1)))
    mes = int(input("Digite o mês de nascimento da pessoa %i: "%(cont+1)))
    ano = int(input("Digite o ano de nascimento da pessoa %i: "%(cont+1)))
    idade = int(input("Digite a idade a ser completada da pessoa %i: "%(cont+1)))

    print("A pessoa %i fará %i anos no dia %i/%i/%i\n" %((cont+1), idade, dia, mes, ano+idade))
    cont += 1
    n += 1
"""
Foi utilizado %i, pois se trata de inteiro
O python trabalha com as seguintes letras:
Para Inteiros --> %i ou %d
Para floats --> %f
Para strings --> %s
"""