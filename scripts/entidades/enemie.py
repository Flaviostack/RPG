import random
import time

class inimigo:
    def __init__(self, classe, vida, ataque, defesa, inventario, localizacao):
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = inventario
        
    def atacar(self, player):
        time.sleep(1)
        sorte = random.randint(1, 10)
        
        if sorte <= 2:
            dano = 0
        elif sorte <= 5:
            dano = self.ataque - (player.defesa*1.2)
        elif sorte <= 9:
            dano = self.ataque
        else:            
            dano = self.ataque + (self.ataque*0.5)
            print(f"{self.classe} deu um ataque crítico em {player.nome}!")
        
        if dano > 0:
            player.vida -= dano
            print(f"{self.classe} atacou {player.nome} e causou {dano} de dano!")
        else:
            print(f"{player.nome} bloqueou o ataque de {self.classe}!")
        
        
                
    def morrer(self, mensagem):
        print(mensagem)
        drop = random.choice(self.inventario)
        print(f"{self.classe} deixou cair {drop}!")
        player.inventario.append(drop)
        self.inventario.clear()