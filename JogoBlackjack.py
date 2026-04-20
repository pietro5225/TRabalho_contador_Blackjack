from Jogador import Jogador
from Crupie import Crupie
from Baralho import Baralho
from MotorProbabilidade import MotorProbabilidade
from ContadorHilo import ContadorHilo
#Classe jogoblackjack: fundamental para controlar a lógica principal do jogo
class JogoBlackjack:
    def __init__(self, quantidade_baralhos: int = 1): 
        self.baralho = Baralho(quantidade_baralhos)
        self.contador_hilo = ContadorHilo()
        self.motor_probabilidade = MotorProbabilidade(self.baralho, self.contador_hilo)
        self.jogador = Jogador("Jogador")
        self.crupie = Crupie()
        self.rodada_encerrada = False

    def reiniciar_rodada(self):
        self.jogador.limpar_mao()
        self.crupie.limpar_mao()
        self.rodada_encerrada = False

    def  iniciar_rodada(self):
        self.reiniciar_rodada()

        if self.baralho.cartas_restantes() < 15:
            quantidade = self.baralho.quantidade_baralhos
            self.baralho = Baralho(quantidade)
            self.contador_hilo.reiniciar()
            self.motor_probabilidade = MotorProbabilidade(self.baralho, self.contador_hilo)

        for _ in range(2):
            self.jogador.comprar(self.baralho, self.contador_hilo)
            self.crupie.comprar(self.baralho, self.contador_hilo)

    def jogador_compra(self):
        if self.rodada_encerrada:
            return
        self.jogador.comprar(self.baralho, self.contador_hilo)
        if self.jogador.mao.melhor_valor() > 21:
            self.rodada_encerrada = True

    def jogador_para(self):
        if self.rodada_encerrada:
            return
        while self.crupie.deve_comprar():
            self.crupie.comprar(self.baralho, self.contador_hilo)
        self.rodada_encerrada = True

    def resultado(self) -> str:
        total_jogador = self.jogador.mao.melhor_valor()
        total_crupie = self.crupie.mao.melhor_valor()

        if self.jogador.mao.melhor_valor() > 21:
            return "Jogador estourou. Crupiê vence."
        if self.crupie.mao.melhor_valor() > 21:
            return "Crupiê estourou. Jogador vence."
        if self.jogador.mao.eh_blackjack() and not self.crupie.mao.eh_blackjack():
            return "Blackjack do jogador. Jogador vence."
        if self.crupie.mao.eh_blackjack() and not self.jogador.mao.eh_blackjack():
            return "Blackjack do crupiê. Crupiê vence."
        if total_jogador > total_crupie:
            return "Jogador vence."
        if total_crupie > total_jogador:
            return "Crupiê vence."
        return "Empate."

    def obter_estado_textual(self, esconder_primeira_carta_crupie: bool = True) -> str:
        resumo = self.motor_probabilidade.obter_resumo_probabilidades(
        self.jogador.mao.melhor_valor()
    )

        cartas_jogador = ", ".join(str(carta) for carta in self.jogador.mao.cartas)

        if esconder_primeira_carta_crupie and len(self.crupie.mao.cartas) >= 2 and not self.rodada_encerrada:
            cartas_crupie = f"{self.crupie.mao.cartas[0]}, [Carta Oculta]"
            total_crupie = "?"
        else:
            cartas_crupie = ", ".join(str(carta) for carta in self.crupie.mao.cartas)
            total_crupie = str(self.crupie.mao.melhor_valor())

        texto = (
            f"================ BLACKJACK ================\n\n"
            f"Jogador:\n"
            f"  Cartas: {cartas_jogador}\n"
            f"  Total : {self.jogador.mao.melhor_valor()}\n\n"
            f"Crupiê:\n"
            f"  Cartas: {cartas_crupie}\n"
            f"  Total : {total_crupie}\n\n"
            f"{resumo}\n"
        )

        return texto
