import random

class Carta:
    """Representa uma carta do baralho com valor e naipe."""

    def __init__(self, valor:int, naipe:str):
        """Inicializa a carta com valor (ex: 'A', '10') e naipe."""
        self.valor = valor
        self.naipe = naipe

    def valor_blackjack(self)-> int:
        """Retorna o valor numérico da carta no Blackjack."""
        if self.valor == 'A':
            return 11
        elif self.valor == 'J' or self.valor == 'Q' or self.valor == 'K':
            return 10
        else:
            return int(self.valor)

    def valor_hilo(self) -> int:
        """Retorna o valor da carta para contagem Hi-Lo."""
        if self.valor in ['2','3','4','5','6']:
            return 1
        elif self.valor in ['7','8','9']:
            return 0
        else:
            return -1

    def __str__(self)-> str:
        """Retorna a representação da carta como texto."""
        return self.valor + " de " + self.naipe
