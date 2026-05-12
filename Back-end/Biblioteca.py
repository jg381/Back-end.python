print("----------SEJA BEM-VINDO(A) A BIBLIOTECA PYTHON!!!----------")

livros = []

while True:
    try:

        print("1 - Cadastrar livro")
        print("2 - Lista de livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Sair")
                
        opcao = input("Escolha uma opção: ")
            
            #CADASTRO DE LIVROS
        if opcao == "1":
            livro_2 = input("Qual o nome do livro?:")
            autor = input("Qual o autor?:")
            quantidade = int(input("Digite a quantidade: "))
            
            livros.append([livro_2, autor, quantidade])
            print("Livro cadastrado!")
            
            # LISTA DE LIVROS
        elif opcao == "2":
            print("\n--- LISTA DE LIVROS ---")
            for livro in livros:
                print(f"Título: {livro[0]} | Autor: {livro[1]} | Quantidade: {livro[2]}")
            
            # EMPRÉSTIMO DE LIVROS
        elif opcao == "3":
            livro_2 = input("Digite o título do livro para empréstimo: ")
            for livro in livros:
                if livro[0] == livro_2:
                    if livro[2] > 0:
                        livro[2] -= 1
                    print("Empréstimo realizado!")
                else:
                    print("Livro inválido/não encontrado")
                break
                
        elif opcao == "4":
            livro_2 = input("Digite o título do livro para devolução: ")
            for livro in livros:
             if livro[0] == livro_2:
                if livro[2] > 0:
                    livro[2] += 1
                    print("Devolução realizada!")
                else:
                    print("Livro inválido/não encontrado")
                break
            
        elif opcao == "5":
                print("Finalizado.")
                break
        else:
                print("Opção Inválida!")
    except ValueError:
        print("Opção inválida")