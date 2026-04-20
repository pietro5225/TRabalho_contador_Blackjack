class ContadorHilo:
    """Controla a contagem de cartas pelo método Hi-Lo."""

    def __init__(self):
        self.contagem_recorrente = 0

    def atualizar(self, carta):
        if carta is not None:
            self.contagem_recorrente += carta.valor_hilo()

    def reiniciar(self):
        self.contagem_recorrente = 0

    def calcular_valor_real(self, cartas_restantes):
        """Calcula o valor real da contagem com base no número de baralhos que faltam."""
        if cartas_restantes <= 0:
            return 0.0

        # Evita que a contagem seja pequena demais.
        baralhos_restantes = max(0.2, cartas_restantes / 52.0)

        return self.contagem_recorrente / baralhos_restantes

    def estimar_vantagem(self, cartas_restantes):
        """Estima a vantagem percentual atual do jogador sobre a mesa."""
        contagem_verdadeira = self.calcular_valor_real(cartas_restantes)
        vantagem_base_cassino = -0.5
        incremento_jogador = 0.5

        return vantagem_base_cassino + (contagem_verdadeira * incremento_jogador)

    def probabilidade_empirica_alta(self, cartas_restantes):
        """Estima a probabilidade da próxima carta ser alta (10, J, Q, K, A)"""
        contagem_verdadeira = self.calcular_valor_real(cartas_restantes)
        estimativa_cartas_altas = 20 + contagem_verdadeira
        probabilidade = estimativa_cartas_altas / 52.0
        probabilidade = max(0.0, min(1.0, probabilidade))
        return probabilidade * 100

    def obter_relatorio_estrategico(self, cartas_restantes):
        """Retorna uma string formatada com os dados do Hi-Lo."""
        vl = self.calcular_valor_real(cartas_restantes)
        vantagem = self.estimar_vantagem(cartas_restantes)
        prob_alta = self.probabilidade_empirica_alta(cartas_restantes)

        relatorio = (
            f"--- Análise Hi-Lo ---\n"
            f"Contagem Corrente : {self.contagem_recorrente}\n"
            f"True Count        : {vl:.2f}\n"
            f"Vantagem Estimada : {vantagem:.2f}%\n"
            f"Prob. Carta Alta  : {prob_alta:.1f}%\n"
            f"---------------------"
        )
        return relatorio
