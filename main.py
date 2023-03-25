ano1 = int(input("Digite um ano: "))
idade = int(input("Digite sua idade: "))
ano2 = int(input("Digite outro ano: "))
nome = input("Qual seu nome: ")

soma = (ano2 - ano1) + idade

if soma < 0:
    print("Idade invalida")
else:
    print(f"{nome}, no ano de {ano2} você terá {soma} anos")
