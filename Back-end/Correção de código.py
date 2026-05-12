#Correção do código

#Nome de variável diferente:
#nome_ttular     valordepo
#nome_titular    valor_depo  # São interpretadas como variáveis diferentes, causando erro ao usar uma que não foi definida.

#Estrutura errada no if:

#if verifica  in ["sim", "s", "si"]:   #Está faltando o operador in, que é usado para verificar se um valor está dentro de uma lista.
     
#Problemas de indentação:
#if valor_saque <= saldo:    
#saldo -= valor_saque     
#else:
#rint("Erro: O valor do depósito deve ser maior que zero.")  #Usa indentação para definir blocos de código. Sem indentação correta, ocorre erro de sintaxe.

#Problema de digitação:
#if operacao == "saca":
     
#O usuário pode digitar “sacar”, mas o código verifica “saca”, causando falha de escrita


#Solicitar o nome do cliente
 
nome_titular = input("Informe o  nome da conta do titular: ")
 
#Abertura da conta(Deposito inicial)
 
deposito_inicial = float(input("Digite o valor de depósito inicial: "))
 
#Validar se é numero
""" if deposito_inicial.replace(".","",1).isdigit():
    deposito_inicial = float(deposito_inicial)
     """
    #Valida se é maior que 0
if deposito_inicial >= 0:
    saldo = deposito_inicial
    print(f"\nSRº {nome_titular}, conta aberta com sucesso!")
    print(f"Saldo atual: R$ {saldo:.2f}")  
else:
    saldo = 0
    print("\nValor inicial inválido. A conta foi aberta com saldo R$ 0.00")
print(30*("-"))
 
""" else:
        print("Valor inválido! Digite um numero") """
 
# 2. Pergunta de Operação
verifica = input(f"SR {nome_titular} deseja relaizar alguma operação? (sim ou não) ").lower()
 
""" if verifica == "sim": """
if verifica in ["sim", "s", "si"]:
    print("Qual operação o Sr. gostaria de realizar? ")
    operacao = input("Opções [Sacar], [Depsitar], [Saldo] ").lower()
 
    # Estrutura de Decisão para Operações
    if operacao in ["saca", "sacar", "saque", "s"]:
        valor_saque = float(input("Informe o valor do saque: R$ "))
        # Verificação de Saldo Insuficiente
        if valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque realizado! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Erro: Saldo insuficiente para esta operação.")
    elif operacao == "depositar":
        valor_depo = float(input("Informe o valor do depósito: R$ "))
       
        # Validação de Depósito Positivo
        if valor_depo > 0:
            saldo += valor_depo  # Aqui usamos o sinal de +
            print(f"Depósito realizado! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Erro: O valor do depósito deve ser maior que zero.")
    elif operacao == "saldo":
            print(f"O seu saldo disponível é: R$ {saldo:.2f}")
 
else:
     print("Atendiemnto encerrado!")
 
print("-" * 30)
 