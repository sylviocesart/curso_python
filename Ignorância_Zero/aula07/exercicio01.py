"""
Este programa irá pedir as quatro notas
bimestrais e mostrar a média
"""
soma = int(input("Digite a primeira nota: "))
soma = soma + int(input("Digite a segunda nota: "))
soma = soma + int(input("Digite a terceira nota: "))
soma = soma + int(input("Digite a quarta nota: "))
media = soma/4
print("A media do aluno foi:",media)



"""
Trabalhando com ponto fluante e arredondando o valor da média

nota1 = float(input("Qual sua nota no primeiro bimestre? "))
nota2 = float(input("Qual sua nota no segundo bimestre? "))
nota3 = float(input("Qual sua nota no terceiro bimestre? "))
nota4 = float(input("Qual sua nota no quarto bimestre? "))

media = float((nota1+nota2+nota3+nota4)/4)

media = round(media)
print("A sua média foi:",media)
"""