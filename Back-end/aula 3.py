#Entrada de dados
n1= float(input("Informe o primeiro valor: "))
n2= float(input("Informe o segundo valor: "))
operação= input("Informe a operação\n(+, -, *, /): ")

#Processamento
if operação == "+": resultado= n1+n2
if operação == "-": resultado= n1-n2
if operação == "*": resultado= n1*n2
if operação == "/": resultado= n1/n2

#Saída 
print(f"Resultado:{operação}: [{resultado}] ")
