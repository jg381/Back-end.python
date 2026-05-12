import random

numero_secreto = random.randrange(10,101)
fichas = 0
pontos = 100
 
nivel = int(input("Escolha um nível: \n 1 - fácil, \n 2 - Médio, \n 3 - Difícil "))
if nivel == 1:
    fichas = 20    
    ganhei = 5
    perdi = 2
elif nivel == 2:
    fichas = 10
    ganhei = 10
    perdi = 5
elif nivel == 3:
    fichas = 5
    ganhei = 15
    perdi = 8
else:
    print("Valor invalido! ")  
 
 
try:
    tentativa = 1
    while tentativa <= fichas:

        palpite = int(input("Informe seu palpite (entre 10 e 100): "))
 
        if palpite < 10 or palpite > 100:
            print("Valor informado esta fora do intervalo de 10 a 100.")
            continue 
        print(f"Tentativa {tentativa} de {fichas}")
        print(30*"-")
   
        if palpite == numero_secreto:
            print("Parabéns!! Você Acertou!")
            pontos += ganhei
            print(f"Sua pontuação atual é: {pontos}")
            break
        elif palpite < numero_secreto:
            print("Você errou, seu palpite é menor que o numero secreto!")
            pontos -= perdi
            print(f"Sua pontuação atual é: {pontos}")
        else:
            print("Você errou, seu palpite é maior que o numero secreto! ")
            pontos -= perdi
            print(f"Sua pontuação atual é: {pontos}")
       
        tentativa += 1
   
    if pontos < 0:
        pontos = 0
   
    print(F"A sua pontução final foi {pontos}")
    print(f"O numero secreto é: {numero_secreto} ")
    print("Fim de jogo!")
 
except ValueError:
    print("Valor Invalido!")