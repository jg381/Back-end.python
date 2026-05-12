
total = 0
totl_itens = 0
qtd_burguer = 0
qtd_batata = 0
qtd_refri = 0

try:
    while True:
        print("\nCadápio:")
        print("\nHambúrguer → R$ 15")
        print("\nRefrigerante → R$ 5")
        print("\nBatata Frita → R$ 7") 

        pedido= input("Qual é o seu pedido? Selecione os itens que deseja, ou escreva finalizar pra encerrar: ").lower()
    
        if pedido in ["fim","finalizar", "f"]:
            break   
        
        if pedido in ["hamburguer","burguer"]:
                qtd_itens = int(input("Quantidade: "))
                totl_itens += qtd_itens
                total += 15 * qtd_itens
                qtd_burguer += qtd_itens
                print(f"Seu pedido está no total de:R${total} \n")

        elif pedido in ["refrigerante","refri"]:
                qtd_itens = int(input("Quantidade: "))
                totl_itens += qtd_itens
                total += 5 * qtd_itens
                qtd_refri += qtd_itens
                print(f"Seu pedido está no total de:R${total} \n")
        
        elif pedido in ["batata frita","batata","fritas"]:
                qtd_itens = int(input("Quantidade: "))
                totl_itens += qtd_itens
                total += 7 * qtd_itens
                qtd_batata += qtd_itens
                print(f"Seu pedido está no total de:R${total} \n")

        else:
            print("Opção incorreta")
    
    #Desconto de 10%
    if total >= 20:
       desconto = total * 0.1
       total -= desconto
    
    print(f"Total do pedido = R${total:.2F}")
    print(f"Total de itens = {totl_itens}")

    if qtd_burguer > 0:
         print(f"Quantidade de Hamburguer:{qtd_burguer}")
         
    if qtd_refri > 0:
         print(f"Quantidade de Refrigerante:{qtd_refri}")

    if qtd_batata > 0:
         print(f"Quantidade de Batata:{qtd_batata}")
    

except ValueError:
    print("Opção inválida!")