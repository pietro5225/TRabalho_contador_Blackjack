from Carta import Carta
class Mao:
    """Representa a mão de um jogador no Blackjack."""

    def __init__(self, dono):
        """Inicializa a mão associada a um jogador."""
        self.dono = dono
        self.cartas = []

    def adicionar_carta(self, carta):
        """Adiciona uma carta à mão."""
        if carta is not None:
            self.cartas.append(carta)

    def limpar(self):
        """Remove todas as cartas da mão."""
        self.cartas = []

    def valor(self):
        """Calcula o valor total da mão considerando regras do Blackjack."""
        total = 0
        ases = 0

        for carta in self.cartas:
            total += carta.valor_blackjack()
            if carta.valor == 'A':
                ases += 1

        while total > 21 and ases > 0:
            total -= 10
            ases -= 1

        return total

    def eh_blackjack(self):
        """Verifica se a mão é um Blackjack (21 com 2 cartas)."""
        return len(self.cartas) == 2 and self.valor() == 21

     def melhor_valor(self) -> int:
         """Retrona o melhor valor possivel da mão no BlackJack"""
         validos = [valor for valor in self.valores_possiveis() if valor <= 21]
         if validos:
             return max(validos)
         return min(self.valores_possiveis())

    def __str__(self):
        """Retorna representação da mão com cartas e valor total."""
        texto = self.dono + ": "

        for carta in self.cartas:
            texto += str(carta) + ", "

        texto += "(Total: " + str(self.valor()) + ")"
        return texto
