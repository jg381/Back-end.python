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

"""class Animal:
    #Método construtor (inicialização)
    def __init__(self, nome_animal, idade_animal, raca_animal, tipo_animal, som_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.raca = raca_animal
        self.tipo = tipo_animal
        self.som = som_animal

    def info_animal(self):
        print(f"O animal {self.nome}, tem a idade de {self.idade}, raça: {self.raca}, som: {self.som} ")
    
    def som_do_animal(self):
        mensagem = f"O animal {self.nome} faz {self.som}"
        return mensagem
    
cachorro = Animal("Fred", "4 meses", "Pitbul", "Cachorro", "AU-AU")
cachorro.info_animal()
print(cachorro.som_do_animal())

print(70*"-")

gato = Animal("Kit", "2 meses", "Desconhecida", "Gato", "miau")
gato.info_animal()
print(gato.som_do_animal())"""

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

class ContaBancaria:
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
 
print(cliente.total_saldo())
 
            