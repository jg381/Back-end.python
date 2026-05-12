# Calcule o IMC (peso / altura²) e classifique:
# <18.5 = Magro | 18.5-24.9 = Normal | 25-29.9 = Sobrepeso | >30 = Obeso
print("Calculador de IMC (índice de massa corporal)")

peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))
# SEU CÓDIGO AQUI
imc = peso / altura**2
try:
    
         if imc < 18.5:
             print("Você é magro!")
        
         elif imc > 18.5 and imc < 24.9:
                print("Você é Normal!")

         elif imc > 18.5 and imc < 29.9:
                print("Você está com Sobrepeso")
            
         else:
              print("Você está obeso")
        
except ValueError:
    print("Valor inválido!")