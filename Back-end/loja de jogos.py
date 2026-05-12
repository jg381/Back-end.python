# Lista de jogos e preços
jogos = ["Minecraft", "GTA V", "FIFA"]
precos = [80, 120, 90]

# total
total = 0

print("Jogos disponíveis:")
for i in range(len(jogos)):
    print(f"{i+1} - {jogos[i]} | R$ {precos[i]}")

print("\nEscolha os jogos para comprar.")
print("Digite 0 para finalizar.\n")

while True:
    escolha = int(input("Digite o número do jogo: "))

    if escolha == 0:
        break

    if 1 <= escolha <= len(jogos):
        total += precos[escolha - 1]
        print(f"{jogos[escolha - 1]} adicionado!")
    else:
        print("Opção inválida!")

# desconto
desconto = 0

if total > 200:
    desconto = total * 0.10

total_final = total - desconto

# Resultado
print("\n--- Tatal da compra ---")
print(f"Total da compra: R$ {total}")

if desconto > 0:
    print(f"Desconto: R$ {desconto:.2f}")

print(f"Total com desconto: R$ {total_final:.2f}")