from animal import Animal

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

print(70*"-")
