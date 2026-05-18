#Sistema Biblioteca

livros = []
emprestados = []

def mensagem(msg):
    print(msg)

def cadastrar_livro(livro):
    livros.append(livro)
    return mensagem("Livro cadastrado")

def mostrar_livros():
    for i in range(len(livros)):
        if livros[i] not in emprestados:
            mensagem(f"{i} - {livros[i]}")

def emprestar_livro(escolha):
    emprestados.append(livros[escolha])

def quantidade_emprestados():
    return len(emprestados)


def menu():
    print("\n==== Biblioteca ====")
    print("1 - Cadastrar Livro")
    print("2 - Mostrar Livros Disponíveis")
    print("3 - Registrar Empréstimo")
    print("4 - Mostrar Quantidade Emprestados")
    print("5 - Sair")


def main():
    while True:
        menu()
        opcao = int(input("Escolha a opção pelo numero: "))

        if opcao == 1:
            livro = input("Nome do livro: ")
            cadastrar_livro(livro)
            mensagem("Livro cadastrado com sucesso")

        elif opcao == 2:
            mensagem("\n==== Livros Disponíveis ====")
            mostrar_livros()

        elif opcao == 3:
            mensagem("\n==== Livros Disponíveis ====")
            mostrar_livros()
            escolha = int(input("Escolha o livro pelo numero: "))
            emprestar_livro(escolha)
            mensagem("Empréstimo realizado!")

        elif opcao == 4:
            mensagem(f"Quantidade de livros emprestados: {quantidade_emprestados()}")

        elif opcao == 5:
            mensagem("Finalizado...")
            break

        else:
            mensagem("Opção invalida!")

main()