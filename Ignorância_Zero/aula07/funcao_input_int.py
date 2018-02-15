"""
Trabalhando com as funções input e int
O "input" escreve uma mensagem na tela e 
aguarda uma resposta
"""

# Função para limpar a tela
import os
os.system("clear")

num1 = input("Entre com um número: ")
print(num1)

# Convertendo a saida em inteiro - int
num2 = int(input("Digite um número: "))
print("O número digitado foi:",num2)