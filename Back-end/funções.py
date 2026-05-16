"""idade = input("Qual sua idade:")
nome = input("Qual seu nome?:")
def usuario(idade,nome):
    print(f"Você tem {idade} anos, e seu nome é {nome}")

usuario(idade,nome)"""


"""produto = input("Qual produto quer cadastrar: ")
vendido = input("Qual produto quer vender?: ")

def cadastro(produto):
    print(f"Produto {produto} cadastrado!!")

def venda(vendido):
    print(f"Produto {vendido} vendido!!!")

def mostrar_calculo(valor_um, valor_dois):
    resultado = valor_um * valor_dois
    print(f"O resultado da conta é {resultado}")

mostrar_calculo(20,10)
cadastro(produto)
venda(vendido)"""


def multiplicar(a, b):
    return a * b

resultado1 = multiplicar(5, 4)
print(resultado1)


def media(n1, n2):
    return (n1 + n2) / 2

resultado2 = media(7, 8)
print(resultado2)


def desconto(valor, porcentagem):
    return valor - (valor * porcentagem / 100)

resultado3 = desconto(100, 20)
print(resultado3)