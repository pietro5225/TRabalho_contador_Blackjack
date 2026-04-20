import random
import Carta
class Baralho:
    """Representa um conjunto de cartas (um ou mais baralhos)."""

    def __init__(self, quantidade_baralhos=1):
        """Inicializa o baralho com uma quantidade de decks."""
        self.quantidade_baralhos = quantidade_baralhos
        self.cartas = []
        self.criar_baralho()
        self.embaralhar()

    def criar_baralho(self):
        """Gera todas as cartas possíveis no baralho."""
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        naipes = ['Copas','Ouros','Paus','Espadas']

        self.cartas = []

        for _ in range(self.quantidade_baralhos):
            for naipe in naipes:
                for valor in valores:
                    self.cartas.append(Carta(valor, naipe))

    def embaralhar(self):
        """Embaralha aleatoriamente as cartas."""
        random.shuffle(self.cartas)

    def comprar_carta(self):
        """Remove e retorna uma carta do topo do baralho."""
        try:
            return self.cartas.pop()
        except IndexError:
            print("Baralho vazio.")
            return None

    def __str__(self):
        """Retorna quantidade de cartas restantes."""
        return "Baralho com " + str(len(self.cartas)) + " cartas"