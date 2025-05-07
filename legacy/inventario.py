# Transformando uma lista de strings em maiúsculas usando list comprehension
import random
import time

inventario = ['lanterna', 'corda', 'barraca', 'faca', 'bife']
inventario = [item.upper() for item in inventario]

print("Você foi atacado por um monstro!")
time.sleep(1)  # Pausa de 1 segundo
print("Você precisa de um item para se defender.")
time.sleep(1)  # Pausa de 1 segundo
print("Você tem os seguintes itens no inventário:")
print(", ".join(inventario))  # Exibe os itens separados por vírgulas

item = input("Qual item você deseja equipar? ").strip().upper()

if item in inventario:
    print(f"Você equipou o item {item}.")
else:
    print(f"Você não tem o item {item} no inventário.")

print(f"Deseja usar o item {item} (s/n)")
resposta = input().strip().lower()

if resposta == 's':
    if item in inventario and item == 'FACA':
        print("Você usou a faca para se defender.")
        time.sleep(1)  # Pausa de 1 segundo
        sorte = random.randint(1, 10)
        
        if sorte < 2:
            print("Você acerta um golpe crítico no monstro!")
            time.sleep(1.5)
            print("O monstro estava fingindo estar ferido...")
            time.sleep(1)  # Pausa de 2 segundos
            print("Ele te atacou e você ficou mortinho da silva!")
        
        elif sorte >= 2 and sorte < 5:
            print("O monstro ficou ferido, mas ainda está vivo...")
            time.sleep(2)  # Pausa de 2 segundos
            print("Ele te atacou e você ficou ferido!")
        
        elif sorte >= 5 and sorte < 9:
            print("O monstro ficou ferido e está mais fraco...")
            time.sleep(2)  # Pausa de 2 segundos
            print("Ele te atacou, mas você conseguiu se defender!")
            print("Você acertou um último golpe no monstro e ele morreu!")
        
        elif sorte == 10:
            print("Você acertou um golpe certeiro no monstro!")
            time.sleep(2)  # Pausa de 2 segundos
            print("Ele ficou muito ferido e não consegue mais te atacar!")
            inventario.remove(item)
            print(f"Você não tem mais o item {item} no inventário, mas...")
            time.sleep(1)  # Pausa de 1 segundo
            print("Você venceu o monstro!")
            print("Você ganhou um item especial!")
            inventario.append('Garras do Monstro')

    elif item in inventario and item == 'CORDA':
        print("Você tenta usar a corda...")
        time.sleep(1)  # Pausa de 1 segundo
        chance = random.randint(1, 10)
        if chance < 5:
            print("Você não conseguiu amarrar o monstro com a corda!")
            print("O monstro roubou a corda, te amarrou e fingiu que você era um iô-io!")
            print("Você ficou tonto e morreu!")
 
            time.sleep(2)  # Pausa de 2 segundos
            print("O monstro te atacou!")
        elif chance >= 5 and chance < 8:
            print("Você amarrou o monstro com a corda, mas ele parece resistente.")
            sorte = random.randint(1, 10)
            if sorte < 5:
                print("O monstro conseguiu se soltar e te atacou!")
                time.sleep(1)
                print("Cê já era, papae!")
            time.sleep(2)  # Pausa de 2 segundos
        
        elif chance >= 8:
            print("Você amarrou o monstro com a corda e conseguiu escapar!")
            time.sleep(2)  # Pausa de 2 segundos
        inventario.remove(item)
        
    elif item in inventario and item != 'FACA' and item != 'CORDA':
        print("pra quê tu vai usar isso contra um monstro??????")
        time.sleep(1)
        print("O monstro te atacou!")
        print("Morreu de burro, chefe!")
        
else:
    print(f"Você não usou o item {item}.")
    time.sleep(1)  # Pausa de 1 segundo
    print(f"Você ainda tem o item {item} no inventário, mas o monstro te atacou!")
    print("Cê morreu papae.")