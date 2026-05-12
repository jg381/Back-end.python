#Peça a idade do usuário e informe se é "Maior de idade" ou "Menor de idade".
idade = int(input("Qual sua idade?: "))


if (idade >= 18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#Peça um número inteiro e informe se ele é positivo, negativo ou zero.

número= int(input("Informe o número: "))

if (número > 0):
    print("Esse número é inteiro")

if (número == 0):   
    print ("Esse número é igual a 0")

if (número < 0):
    print ("Esse número é negativo")

#Crie uma variável senha = "python123". Peça ao usuário para digitar a senha e informe se está correta ou incorreta.

senha = input("Qual é a senha?: ")

if (senha == "python123"):
    print ("Senha correta")

else:
    print ("Senha incorreta")

#Peça um número ao usuário e informe se ele é par ou ímpar.

número = int(input("Informe um número: "))

if (número % 2) == 0:
    print("É um número par.")

else:
    print("É um número ímpar.")

#Sistema de login

 
login = input("Informe seu usuario: ")
passwd = input("informe sua senha: ")
usuario= "jg"
senha= 123
 
if usuario == login:
    print("usuario correto")
    if senha == passwd:
        print("senha correta")
    else:
        print("senha incorreta")
else:
    print("usuário incorreto")
 
 #Jogo de adivinhação

print("Descubra o valor Secreto\nTente adivinhar o número correto!\nDe 1 a 10")

numero_secreto = 3

try:
    palpite = int(input("Qual o seu palpite?: "))

    if palpite == numero_secreto:
        print("PARABÉNS VOCÊ ACERTOU!!!")

    elif palpite > numero_secreto:
        print("O número secreto é menor que seu palpite!")

    elif palpite < numero_secreto:
        print("O número secreto é maior que seu palpite!")

except ValueError:
    print("Valor inválido")
#Professor, esse código foi feito praticamente sozinho,só não consegui fazer a "execeção" sem pesquisar.