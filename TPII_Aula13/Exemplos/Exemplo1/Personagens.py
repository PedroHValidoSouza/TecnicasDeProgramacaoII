
class Personagem:
    def __init__(self, tipo, arma):
        self.tipo = tipo
        self.arma = arma

    def exibir(self, x, y):
        return f"{self.tipo} usando {self.arma} na coordenada {x}, {y}"

class FabricaPersonagem:
    Personagens = {}

    @classmethod
    def obter_Personagem(cls, tipo, arma):
        chave = (tipo, arma)

        if chave not in cls.Personagens:
            cls.Personagens[chave] = Personagem(tipo, arma)
            print("Novo tipo de personagem criado")
    
        return cls.Personagens[chave]

player_1 = FabricaPersonagem.obter_Personagem(
    "Guerreiro", "Espada"
)

player_2 = FabricaPersonagem.obter_Personagem(
    "Guerreiro", "Espada"
)

player_3 = FabricaPersonagem.obter_Personagem(
    "Mago", "Cajado"
)

player_4 = FabricaPersonagem.obter_Personagem(
    "Guerreiro", "Espada"
)

print(player_1.exibir(20, 20))
print(player_2.exibir(12, 30))
print(player_3.exibir(24, 1))
print(player_4.exibir(13, 50))
#