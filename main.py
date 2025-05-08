import time
import random
from scripts.entidades import player
from scripts.entidades import enemie

jogador = player.player("Jogador", 10, 2, 10, ["Pedra", "graveto"], "Estrada") #nome, vida, ataque, defesa, inventario, localizacao
jogador.inventario = [item.upper() for item in jogador.inventario]  # Converte os itens para maiúsculas

monstro1 = enemie.inimigo("Ogro", 12, 4, 1, ["Carne", "Garras de Monstro"])# #nome, vida, ataque, defesa, inventario
monstro1.inventario = [item.upper() for item in monstro1.inventario]  # Converte os itens para maiúsculas

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
        sorte = random.randint(4, 8)
        if sorte <= 3:
            print("Você tentou atirar uma pedra no monstro. Ele não se machucou.")
            time.sleep(1)
            print(f"o {monstro1.classe} aprendeu com o seu ataque. ")
            time.sleep(1)
            print(f"Ele pega uma pedra maior e atira em você.")
            jogador.vida = jogador.vida - jogador.vida
            time.sleep(1)
            print(f"Você ficou com {jogador.vida}hp")
            if jogador.vida <= 0:
                jogador.morrer("Você morreu.")
        if sorte >3 and sorte <= 8:
            
            jogador.ataque = jogador.ataque + (sorte/2)
            jogador.atacar(monstro1, "Você atirou uma pedra no monstro.")
            time.sleep(1)
            print(f"o {monstro1.classe} levou {jogador.ataque-monstro1.defesa} de dano e ficou com {monstro1.vida}hp")            
            '''
            print("Você atirou uma pedra no monstro. Ele se machucou.")
            time.sleep(1)
            jogador.ataque = jogador.ataque + sorte
            monstro1.vida = monstro1.vida - jogador.ataque
            print(f"o {monstro1.classe} perdeu {jogador.atacar} ficou com {monstro1.vida}hp")
            time.sleep(1)
            if monstro1.vida <= 0:
                monstro1.morrer("Você matou o monstro.")
                        '''
            
            
        jogador.ataque = jogador.ataque + 3
        time.sleep(1)  # Pausa de 1 segundo