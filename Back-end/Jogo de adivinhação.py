import random


print("Descubra o valor Secreto\nTente adivinhar o número correto!\nDe 1 a 10")

numero_secreto = 3

try:
    palpite = int(input("Qual o seu palpite?: "))

    if palpite == numero_secreto:
        print("PARABÉNS VOCÊ ACERTOU!!!")

    elif palpite > numero_secreto:
        print("O número secreto é menor que seu palpite!")

    else:
        print("O número secreto é maior que seu palpite!")

except ValueError:
    print("Valor inválido")
#Professor, esse código foi feito praticamente sozinho,só não consegui fazer a "execeção" sem pesquisar.
# O numero secreto deverá ser aleatório
# 1 - Pesquisar sobre a função random - Servir para gerar um numero aleatório
# 2 - Permitir que o usuario escolha um numero entre 10 e 100, se ele jogar um numero menor que 10 ou maior que 100 informe que o vlaor é invalido
 
# Dica o random permite estabelecer um inicio e um fim
# pesquisar como limitar os valores entre 10 e 100 no random
 
 
print("Descubra o valor Secreto\nTente adivinhar o número correto!\nDe 10 a 100")

numero_secreto = random.randint(10, 100)

try:
    palpite = int(input("Qual o seu palpite?: "))

    if palpite < 10 or palpite > 100:
        print("Valor inválido")

    elif palpite == numero_secreto:
        print("PARABÉNS VOCÊ ACERTOU!!!")

    elif palpite > numero_secreto:
        print("O número secreto é menor que seu palpite!")

    else:
        print("O número secreto é maior que seu palpite!")

except ValueError:
    print("Valor inválido")