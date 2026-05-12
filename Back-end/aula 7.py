"""controlador = True
 
while controlador:
 
    try:
        n1 = int(input("Informe o primeiro valor: "))
        n2 = int(input("Informe o segundo valor: "))
 
        if n1>n2:
            n3 = n1
            n1 = n2
            n2 = n3
 
        for i in range(n1,n2 +1 ):
            if i % 2 == 0:
                print(i)
            controlador = False
 
    except ValueError:
        print("Valor inválido!") """


candidato_um = 0
candidato_dois = 0
candidato_tres = 0
 
for i in range(5):
    voto = int(input("Digite seu voto: [1],[2],[3]: "))
    if voto == 1:
        candidato_um += 1
    elif voto == 2:
        candidato_dois += 1
    elif voto == 3:
        candidato_tres += 1
    else:
        print("Candidadto invalido! ")
 
print("Candidato 1: ", candidato_um)
print("Candidato 2: ", candidato_dois)
print("Candidato 3: ", candidato_tres)