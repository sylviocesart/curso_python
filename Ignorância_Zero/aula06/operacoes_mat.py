# Declarando duas variáveis na mesma linha
# Somando dois números
num1, num2 = 5,30
soma = num1 + num2
print("A soma dos números",num1,"e",num2,"foi:",soma)

# Subtraindo dois números
num1, num2 = 40,2
sub = num1 - num2
print("A subtracao dos números",num1,"e",num2,"foi:",sub)

# Multiplicando dois números
num1, num2 = 2,7
print("A multiplicação dos números",num1,"e",num2,"foi:",num1*num2)
# Ou posso fazer como variável o resultado.
multi = (num1*num2)
print("A multiplicaçãoo dos números",num1,"e",num2,"foi:",multi)

# Divisão
num1, num2 = 10,3
div = num1/num2
# A saída teve casa decimal
print("A divisão dos números foi:",div)
"""
Para tirar a casa decimal, declare a variável como sendo
do tipo inteiro
"""
div_inteira = num1//num2
print("A divisão dos números foi:",div_inteira)

# Obtendo o resto da divisão de dois números
num1, num2 = 10,3
rest = num1%num2
print("O resto da divisão dos números foi:",rest)

# Potência de números
num1, num2 = 10,3
pot = num1**num2
print("A potência dos dois números foi:",pot)

# Juntando as operações em uma só
num1, num2, num3, num4 = 10,5,3,15
multi = (num1+num2)*num3 / num4
print("A operação teve o resultado:", multi)
multi_int = (num1+num2)*num3 // num4
print("A operação teve o resultado:", multi_int)
