"""
# Aprendendo trabalhar com comparações múltiplas
# Verificando se a idade é menor ou maior de idade ou idoso
valor = int(input("Digite sua idade: "))
if 0 < valor < 18:
    print("Você é menor de idade!!\n\n")
else:
    if valor > 70:
        print("Você é idoso!!\n\n")
    else:
        print("Você é maior de idade\n\n")

## Vamos atribuir uma condição, se for maior ou igual a 18 e menor que 70
## então, terá direito a um benefício
# Caso seja diferente, não terá o benefício
idade = int(input("Digite sua idade: "))

if 18 <= idade < 70:
    print("Você terá direito ao benefício\n\n")
else:
    print("Você não terá direito ao benefício\n\n")

## Agora, juntando ambos e formando um só programa
"""
idade = int(input("Digite sua idade: "))
if 18 <= idade < 70:
    print("Você terá o benefício, pois é maior de idade\n\n")
if idade > 70:
    print("Você não terá direito ao benefício, pois é idoso\n\n")
if idade < 18:
    print("Você não terá o benefício, pois é menor de idade!!\n\n")
    