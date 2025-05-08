import random
import time

class player:
    def __init__(self, nome, vida, ataque, defesa, inventario, localizacao):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = inventario
        self.localizacao = localizacao
        
    inventario = ["slot1", "slot2", "slot3", "slot4", "slot5"]
#    armadura = ["SlotBotas", "SlotPeitoral", "SlotCapacete", "SlotLuvas"]
     
    def atacar(self, inimigo, mensagem_de_ataque):
        dano = self.ataque - inimigo.defesa
        time.sleep(1)
        print(mensagem_de_ataque)
        inimigo.vida -= dano
        return dano
    
    def morrer(self, mensagem):
        print(mensagem)
        self.inventario = []
        
    