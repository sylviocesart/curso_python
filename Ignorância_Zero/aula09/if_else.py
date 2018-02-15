"""
Aprendendo a trabalhar com condições.
Juntando o que aprendemos na aula anterior que
falava sobre variáveis booleanas.

idade = int(input("Digite sua idade: "))
resp = idade >= 18
print(resp)

Vamos implementar as condições para as 
respostas

idade = int(input("Digite sua idade: "))
resp = idade >= 18
if resp == True:
    print("Pode entrar!!")

if resp == False:
    print("Não pode entrar!!")

## Agora vamos dá uma sofisticada

idade = int(input("Digite sua idade: "))
resp = idade >= 18
if resp:
    print("Pode beber a vontade")
if resp != True:
    print("Você só pode beber suco!!")


Agora, usando o if com else e declarando a condição
diretamente no "if"

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode beber a vontade")
else:
    print("Você só pode beber suco!!")

Agora vamos incluir uma terceira condição, incluir maior que 21
Porém a resposta, caso a idade seja maior que 18, o programa 
encontrará duas respostas, a de maior que 18 e maior que 21

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode beber a vontade")
if idade >= 21:
    print("Você é VIP")
if idade < 18:
    print("Você só pode beber suco!!")

Vamos melhorar e implementar um if dentro de outro if e 
usar o "else"
"""
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode beber a vontade")
    if idade >= 21:
        print("Você é VIP")
else:
    print("Você só pode beber suco!!")