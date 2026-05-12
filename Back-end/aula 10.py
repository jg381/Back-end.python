#numeros = [10, 20, 30, 40, 50]
#maior_nmr = max(numeros)
#print(maior_nmr)

#menor_nmr = min(numeros)
#print(menor_nmr)

numeros = []
media = 0
for i in range(4):
    nmrs = int(input("Informe os números: "))

    numeros.append(nmrs)
    soma = sum(numeros)
    media = sum(numeros) / len(numeros)
print(numeros)
print(soma)
print(media)
nmrs.pop(2)