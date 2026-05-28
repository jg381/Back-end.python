class Animal:
    #Método construtor (inicialização)
    def __init__(self, nome_animal, idade_animal,tipo_animal,):
        self.nome = nome_animal
        self.idade = idade_animal
        self.tipo = tipo_animal

    def info_animal(self):
        print(f"O animal {self.nome}, tem a idade de {self.idade}, tipo: {self.tipo} ")