#Variaveis
ano1 = int(input("Em que ano estamos?: "))
idade= int(input("Digite sua idade: "))
ano2 = int(input("Digite um ano para prever sua idade: "))
nome = input("Digite seu nome: ")
#Calculos
ano3 = abs(ano1 - ano2)
soma = ano3 + idade
#Resultados
print(f"{nome}, no ano de {ano2} você tera {soma} anos")
