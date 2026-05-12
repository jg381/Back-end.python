# Lista para armazenar os livros
livros = []

while True:
    print("\n--- MENU BIBLIOTECA ---")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # 1 - Cadastrar livro
    if opcao == "1":
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        quantidade = int(input("Digite a quantidade: "))

        livros.append([titulo, autor, quantidade])
        print("Livro cadastrado com sucesso!")

    # 2 - Listar livros
    elif opcao == "2":
        print("\n--- LISTA DE LIVROS ---")
        for livro in livros:
            print(f"Título: {livro[0]} | Autor: {livro[1]} | Quantidade: {livro[2]}")

    # 3 - Empréstimo
    elif opcao == "3":
        titulo = input("Digite o título do livro para empréstimo: ")

        for livro in livros:
            if livro[0] == titulo:
                if livro[2] > 0:
                    livro[2] -= 1
                    print("Empréstimo realizado!")
                else:
                    print("Livro indisponível!")
                break
        else:
            print("Livro não encontrado!")

    # 4 - Devolução
    elif opcao == "4":
        titulo = input("Digite o título do livro para devolução: ")

        for livro in livros:
            if livro[0] == titulo:
                livro[2] += 1
                print("Devolução realizada!")
                break
        else:
            print("Livro não encontrado!")

    # 5 - Sair
    elif opcao == "5":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")