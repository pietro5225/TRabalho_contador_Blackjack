import Jogador
#Classe crupiê: fundamental para definir conceitos e ações sobre o crupiê
class Crupie(Jogador):
    def _init_(self):
        super()._init_("Crupiê")

    def deve_comprar(self) -> bool:
        return self.mao.melhor_valor() < 17