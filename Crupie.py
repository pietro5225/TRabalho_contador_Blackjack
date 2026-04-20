from Jogador import Jogador
#Classe crupiê: fundamental para definir conceitos e ações sobre o crupiê
class Crupie(Jogador):
    def __init__(self):
        super().__init__("Crupiê")

    def deve_comprar(self) -> bool:
        return self.mao.melhor_valor() < 17