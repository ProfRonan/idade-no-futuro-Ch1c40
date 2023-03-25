ano1 = int(input())
idade = int(input())
ano2 = int(input())
nome = input()

soma = (ano2 - ano1) + idade

if soma < 0:
    print("Idade invalida")
else:
    print(f"{nome}, no ano de {ano2} você terá {soma} anos")
