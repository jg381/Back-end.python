class Calculadora:
    def __init__(self, numero1, numero2):
    
        self.numero_um = numero1
        self.numero_dois = numero2

    def soma(self):
        resultado = self.numero_um + self.numero_dois
        return resultado
    
    def subtracao(self):
        resultado = self.numero_um - self.numero_dois
        return resultado
   
    def multiplicacao(self):
        resultado = self.numero_um * self.numero_dois
        return resultado
    
    def divisão(self):
        if self.numero_dois == 0:
            mensagem = "Impossível divisão por zero"
        
        else:
            resultado = self.numero_um / self.numero_dois
            return resultado
        
print("===========CALCULADORA COM CLASSE========== ")


valor_um = int(input("Informe o primeiro valor:"))
valor_dois = int(input("Informe segundo valor:"))

calculador_python = Calculadora(valor_um, valor_dois)

print(f"O resultado da soma é {calculador_python.soma()}")
print(f"O resultado da subtração é {calculador_python.subtracao()}")
print(f"O resultado da multiplicação é {calculador_python.multiplicacao()}")
print(f"O resultado da divisão é {calculador_python.divisão()}")