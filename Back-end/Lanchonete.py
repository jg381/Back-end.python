total = 0
 
 
try:
    while True:
        pedido = input("CARDÁPIO:\nHamburguer= R$30\nRefrigerante= R$15\nBatata Frita= R$7\nCaso queria finalizar o pedido digite: finalizar\nInforme qual o seu pedido:").lower()
 
        if pedido in ["fim","finalizar", "f"]:
               break
 
        if pedido in ["hamburguer","burguer"]:
                total += 30
                print(f"Seu pedido está no total de:R${total} \n")
        elif pedido in ["refrigerante","refri"]:
                total += 15
                print(f"Seu pedido está no total de:R${total} \n")
        elif pedido in ["batata frita","batata","fritas"]:
                total += 7
                print(f"Seu pedido está no total de:R${total} \n")
        else:
            print("Opção incorreta")
 
    print(f"Total do pedido = R${total:.2F}")
         
except ValueError:
        print("Pedido finalizado")
        