def menu():
    print("\n" + "=" * 30)
    print("        MENU DA LOJA")
    print("=" * 30)
    print("1 - Cadastrar Produto")
    print("2 - Sair")
    print("=" * 30)


def desconto(valor):
    if valor >= 100:
        return valor * 0.10
    return 0


while True:
    menu()

    op = input("Escolha uma opção: ")

    if op == "1":
        print("\n--- CADASTRO DE PRODUTO ---")

        nome = input("Produto: ")
        preco = float(input("Preço: R$ "))
        qtd = int(input("Quantidade: "))

        total = preco * qtd
        desc = desconto(total)

        print("\n" + "=" * 30)
        print("      RESUMO DA COMPRA")
        print("=" * 30)
        print("Produto    :", nome)
        print("Total      : R$", total)
        print("Desconto   : R$", desc)
        print("Valor Final: R$", total - desc)
        print("=" * 30)

    elif op == "2":
        print("\nFinalizado.")
        break

    else:
        print("\nOpção inválida!")