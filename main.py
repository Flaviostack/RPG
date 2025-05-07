import time
import random
from scripts.entidades import player
from scripts.entidades import enemie

jogador = player.player("Jogador", 10, 2, 10, ["Pedra", "graveto"], "Estrada")
jogador.inventario = [item.upper() for item in jogador.inventario]  # Converte os itens para maiúsculas

monstro1 = enemie.inimigo("Ogro", 12, 4, 1, ["Carne", "Garras de Monstro"])

print("você acorda em um lugar desconhecido, sem saber como chegou ali.")
print("você se levanta e olha ao seu redor, não há nada a vista, apenas uma estrada de terra.")
print("um monstro aparece na sua frente, ele parece muito forte.")
print("você tenta correr, mas ele te ataca antes.")
print(f"Seu inimigo é um {monstro1.classe} e ele tem {monstro1.vida}hp")

print("Você tem os seguintes itens:")
print(",".join(jogador.inventario))  # Exibe os itens separados por vírgulas
print("Qual item você deseja usar?")

item = input().strip().upper()

if item in jogador.inventario:
    print(f"Você usou o item {item}.")
    if item == "PEDRA":
        jogador.ataque = jogador.ataque + 3
        jogador.atacar(monstro1, "Você atacou o monstro com uma pedra!")
        time.sleep(1)  # Pausa de 1 segundo