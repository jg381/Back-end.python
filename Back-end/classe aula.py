"""class Pessoa:
    def falar(self):

        print("Oi! Estou falando")

pessoa_um = Pessoa()
pessoa_um.falar()

class Animal:
    def som(self):
        print( "*Uivo*")

lobo_um = Animal()
lobo_um.som()

class Computador:
    def digitar(self):
        print("Escrevendo...")
    
pc = Computador()
pc.digitar()

class Celular:
    def ligando(self):
        print("iniciando...")

iphone = Celular()
iphone.ligando()"""


"""class Produto:

    def __init__(self, nome_produto, preco_produto):
            self.nome = nome_produto
            self.preco = preco_produto
        
class Livro:
      def __init__(self, nome_livro, preco_livro):
        
            self.livro = nome_livro
            self.valor = preco_livro

class Filme:
      def __init__(self, nome_filme, tipo_filme):
        
            self.filme = nome_filme
            self.categoria = tipo_filme"""

""" class ContaBancaria:
    def __init__(self):
        self.saldo =  0        
 
    def total_saldo(self):
        mensagem = f"O saldo atual é de R$ {self.saldo}"
        return mensagem
   
    def sobre_deposito(self):
        valor = int(input("Informe o valor a depositar: R$"))
 
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} foi feito")  
        else:
            print("Não foi possivel fazer esse depósito")
 
cliente = ContaBancaria()
 
print(f"Antes do deposito {cliente.total_saldo()}")
cliente.sobre_deposito()
 
print(cliente.total_saldo())"""

"""class ContaBancaria:
    def __init__(self):
        self.__saldo = 0 #Atributo privado (So pode ser alterado atraves de um metodo)
        self.titular = ""
 
    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso")
        else:
            print("Valor de deposito invalido!")
   
    def saque(self, valor_saque):
        if valor_saque > 0 and valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            print(f"Saque de R${valor_saque} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor invalido")
   
    def consulta_saldo(self):
        print(f"Titular: {self.titular}\nSaldo Atual R${self.__saldo}")
 
    def main(self):
        nome_cliente = input("Informe o nome do titular da conta: ")
        while True:
            opcao = int(input("Escolha um opção:\n[1 - Depositar ]\n[2 - Sacar]\n[3 - Mostrar Saldo ]\n[4 - Sair]"))
 
            self.titular = nome_cliente
 
            if opcao == 1:
                valor = float(input("Informe o valor de deposito R$"))
                self.depositar(valor)
            elif opcao == 2:
                valor = float(input("Informe o valor de saque R$"))
                self.saque(valor)
            elif opcao == 3:
                self.consulta_saldo()
            elif opcao == 4:
                print(f"Encerando a sessão! Ate breve Sr {self.titular}")
                break
            else:
                print("Opção invalida!")
 
 
#Fora da classel
cliente = ContaBancaria()
cliente.main()"""
 

"""class Animal:
    #Método construtor (inicialização)
    def __init__(self, nome_animal, idade_animal,tipo_animal,):
        self.nome = nome_animal
        self.idade = idade_animal
        self.tipo = tipo_animal

    def info_animal(self):
        print(f"O animal {self.nome}, tem a idade de {self.idade}, tipo: {self.tipo} ")

class Petshop:
    def __init__(self):
        self.dados_animais = [] #armazena os dados
    
    def cadastrar(self):
        self.cadastro_nome_animal = input("Informe o nome do seu animal:")
        self.cadastro_idade_animal = input("Informe o idade do seu animal:")
        self.cadastro_tipo_animal = input("Informe o tipo do seu animal:")
        
        meu_animal = Animal(
            self.cadastro_nome_animal,
            self.cadastro_idade_animal,
            self.cadastro_tipo_animal
        )
        self.dados_animais.append(meu_animal)

    def mostre_animal(self):
            
        for animal in self.dados_animais:
            animal.info_animal()
    

pet = Petshop()

pet.cadastrar()

pet.mostre_animal()

print(70*"-")"""

from petshop import Petshop