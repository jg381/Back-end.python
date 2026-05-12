
print("---------- DESCUBRA QUAIS SÃO OS PRATO SECRETOS! --------------------")
print("Obs.: Você terá 5 tentativas para tentar acertar 1 dos 5 pratos escolhidos!!!")
 
import random
tentativas = 5
pratos = ["pizza","sushi", "tacos","hamburguer","bolo"]
prato_certo = random.choice(pratos)
 
try:
   
    while tentativas > 0:      
 
     palpite = input("Qual é o seu palpite?: ").lower
 
     if palpite == prato_certo:
            print("Você acerto!! NICEEEE")          
            break
     
     elif palpite != prato_certo:
            tentativas -= 1          
            print("vishh, não foi dessa vez, tente mais uma vez!")
            print(f"você ainda tem {tentativas} tentativas")  
           
           
    print(f"O prato certo é:{prato_certo} ")
 
       
except ValueError:
       print ("Prato Invalido")