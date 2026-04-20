from ContadorHilo import ContadorHilo
from Carta import Carta

class MotorProbabilidade:
    def __init__(self, baralho, contador_hilo):
        self.baralho = baralho
        self.contador_hilo = contador_hilo

    def calcular_probabilidades_reais(self, mao_atual):
        baralho_atual = len(self.baralho.cartas)
        cartas_perde = 0
        limite = 21 - mao_atual  

        for carta in self.baralho.cartas: 
            if carta.valor_blackjack() > limite:
                cartas_perde += 1

        return (cartas_perde / baralho_atual) * 100

    def probabilidade_carta_alta(self):
        baralho_atual = len(self.baralho.cartas)
        cartas_altas = 0

        for carta in self.baralho.cartas:
            if carta.valor_blackjack() >= 10:
                cartas_altas += 1

        return (cartas_altas / baralho_atual) * 100

    def probabilidade_hilo(self):
        """
        Estima probabilidade de carta alta baseada no True Count.
        Modelo linear simples.
        """

        cartas_restantes = len(self.baralho.cartas)
        tc = self.contador_hilo.calcular_valor_real(cartas_restantes)

        # base aproximada de cartas altas em baralho normal (~38%)
        base = 38.0

        # ajuste por True Count (cada ponto ≈ 1.5% de variação)
        ajuste = tc * 1.5

        prob = base + ajuste

        # clamp entre 0 e 100
        return max(0.0, min(100.0, prob))

    def probabilidade_cada_carta(self):
        baralho_atual = len(self.baralho.cartas)
        valores = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        probababilidades_por_carta = {}

        for valor_alvo in valores:
            encontradas = 0
            for carta in self.baralho.cartas:
                if carta.valor == valor_alvo:
                    encontradas += 1

            probababilidades_por_carta[valor_alvo] = (encontradas / baralho_atual) * 100

        return probababilidades_por_carta

    def probabilidade_calculada(self):
        return (
            self.probabilidade_carta_alta()
            - self.contador_hilo.probabilidade_empirica_alta(len(self.baralho.cartas))
        )

    def obter_resumo_probabilidades(self, mao_atual):
        chance_estourar = self.calcular_probabilidades_reais(mao_atual)
        chance_alta_real = self.probabilidade_carta_alta()
        chance_hilo = self.probabilidade_hilo()
        dif_hilo = self.probabilidade_calculada()

        resumo = (
            "------------------------------\n"
            f"Risco de estourar: {chance_estourar:.1f}%\n"
            f"Chance real de carta alta: {chance_alta_real:.1f}%\n"
            f"Estimativa Hi-Lo (carta alta): {chance_hilo:.1f}%\n"
            f"Diferença Hi-Lo vs real: {dif_hilo:.2f}%\n"
            "------------------------------"
        )

        return resumo
