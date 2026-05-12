#ESTRUTURA DE REPETIÇÃO(Loops)#Mostre na tela os números de 1 a 10 usando for.
print("\n""Mostre na tela os números de 1 a 10 usando for")

for i in range (1,11):
      print(i)


print("\n Mostre Mostre os números de 10 até 1 (Ordem decrescente)")

for i in range (10,0, -1):
    print(i)
    
print("Exiba a tabuada do número 5 (de 1 a 10).")

for i in range(1,11):
     print("5x",i,"=",5 *i)

print("\n""Mostre apenas os números pares de 0 a 20")
for i in range(0,21,2):
    print(i)

print("5 números")
num1= float(input("Informe o primeiro número:",)) 
num2= float(input("Informe o segundo número:",)) 
num3= float(input("Informe o terceiro número:",)) 
num4= float(input("Informe o quarto número:",)) 
num5= float(input("Informe o quinto número:",)) 

soma= num1+num2+num3+num4+num5
print("A soma é:",soma)


n_tabuada=int(input('Digite um numero para ver a tabuada: '))
for i in range(1,11):
     print(n_tabuada, "x" ,i,"=",n_tabuada *i)

