ano1 = int(input("Digite o ano estamos: "))
idade= int(input("Digite sua idade: "))
ano2 = int(input("Digite um ano para prever sua idade: "))
nome = (input("Digite seu nome: "))
nome = str(nome)

idade2 = (ano2 - ano1) + idade

print(f"{nome}, no ano de {ano2} você terá {idade2} anos")
