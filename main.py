ano1 = int(input("Digite o ano estamos: "))
idade= int(input("Digite sua idade: "))
ano2 = int(input("Digite um ano para prever sua idade: "))
nome = str(input("Digite seu nome: "))

ano3 = (ano2 - ano1)
soma = ano3 + idade

print(nome, "no ano de ", ano2, "você tera ", soma, " anos")
