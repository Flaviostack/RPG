class player:
    vida = 100
    ataque = 5
    defesa = 0
    inventario = ["slot1", "slot2", "slot3", "slot4", "slot5"]
#    armadura = ["SlotBotas", "SlotPeitoral", "SlotCapacete", "SlotLuvas"]
    
    localizacao = "inicial"
    
    def __init__(self, vida, ataque, defesa, inventario, localizacao):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = inventario
        self.localizacao = localizacao
    
    def atacar(self, inimigo):
        dano = self.ataque - inimigo.defesa
    
    def morrer(self, mensagem):
        print(mensagem)
        self.inventario = []