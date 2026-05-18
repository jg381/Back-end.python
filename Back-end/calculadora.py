#criamos a função
def calculo(num1, operador, num2,):
    if operador == "+":
        resultado = num1 + num2
        return resultado
    
    elif operador == "-":
        resultado = num1 - num2
        return resultado
    
    elif operador == "*":
        resultado = num1 * num2
        return resultado
    
    elif operador == "/":
       #evita um erro
        if num2 == 0:
            #boa prática
            mensagem = "Não é possível dividir por zero!"
            return mensagem
        else:
            resultado = num1 / num2
            return resultado
    
#programação
def main():
    print("BEM VINDO(A) A CALCULADORA PYTHON!!!")
    valor_1 = int(input("Informe o primeiro valor: "))
    operacao = input("Informe a operação (+) (-) (*) (/):")
    valor_2 = int(input("Informe o segundo valor: "))

    print(f"O resultado é: {calculo(valor_1,operacao,valor_2)}")

main()