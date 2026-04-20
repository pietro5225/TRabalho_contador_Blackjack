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

    def valorespossiveis(self):
    """Calcula o melhor valor possível da mão no Blackjack."""
    total_base = 0
    ases = 0

    # soma base sem considerar os ases
    for carta in self.cartas:
        if carta.valor == "A":
            ases += 1
        else:
            total_base += carta.valor_blackjack()

    totais = [total_base]

    # gera todas combinações possíveis dos ases
    for _ in range(ases):
        novos_totais = []
        for total in totais:
            novos_totais.append(total + 1)
            novos_totais.append(total + 11)
        totais = novos_totais

    # filtra valores válidos (<=21)
    validos = [v for v in totais if v <= 21]

    if validos:
        return max(validos)

    return min(totais)

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
