from Jogador import Jogador
from Crupie import Crupie
from Baralho import Baralho
from MotorProbabilidade import MotorProbabilidade
from ContadorHilo import ContadorHilo

# Classe jogoblackjack: fundamental para controlar a lógica principal do jogo
class JogoBlackjack:
    """
    Classe responsável por controlar a lógica principal do jogo de Blackjack.

    Essa classe gerencia:
    - Criação e reposição do baralho
    - Controle da rodada
    - Ações do jogador e do crupiê
    - Contagem de cartas (Hi-Lo)
    - Cálculo de probabilidades
    - Determinação do resultado da rodada

    Atributos:
    ----------
    baralho : Baralho
        Baralho utilizado no jogo.
    contador_hilo : ContadorHilo
        Sistema de contagem de cartas.
    motor_probabilidade : MotorProbabilidade
        Responsável por calcular probabilidades com base no estado atual.
    jogador : Jogador
        Jogador principal.
    crupie : Crupie
        Dealer do jogo.
    rodada_encerrada : bool
        Indica se a rodada atual já foi finalizada.

    Métodos principais:
    ----------
    iniciar_rodada()
        Inicializa uma nova rodada distribuindo cartas.

    jogador_compra()
        Faz o jogador comprar uma carta.

    jogador_para()
        Encerra a vez do jogador e executa a lógica do crupiê.

    resultado() -> str
        Retorna o resultado final da rodada.

    obter_estado_textual() -> str
        Retorna uma representação detalhada do estado atual do jogo.
    """

    def __init__(self, quantidade_baralhos: int):
        """
        Inicializa o jogo de Blackjack.

        Parâmetros:
        ----------
        quantidade_baralhos : int
            Número de baralhos utilizados no jogo.
        """
        self.baralho = Baralho(quantidade_baralhos)
        self.contador_hilo = ContadorHilo()
        self.motor_probabilidade = MotorProbabilidade(self.baralho, self.contador_hilo)
        self.jogador = Jogador("Jogador")
        self.crupie = Crupie()
        self.rodada_encerrada = False

    def reiniciar_rodada(self):
        """
        Reinicia a rodada limpando as mãos dos jogadores
        e liberando o estado para uma nova rodada.
        """
        self.jogador.limpar_mao()
        self.crupie.limpar_mao()
        self.rodada_encerrada = False

    def iniciar_rodada(self):
        """
        Inicia uma nova rodada.

        - Reinicia o estado do jogo
        - Recria o baralho se houver poucas cartas restantes
        - Distribui duas cartas para jogador e crupiê
        """
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
        """
        Faz o jogador comprar uma carta.

        Se o jogador ultrapassar 21 pontos, a rodada é encerrada automaticamente.
        """
        if self.rodada_encerrada:
            return

        self.jogador.comprar(self.baralho, self.contador_hilo)

        if self.jogador.mao.melhor_valor() > 21:
            self.rodada_encerrada = True

    def jogador_para(self):
        """
        Encerra a vez do jogador e executa a lógica do crupiê.

        O crupiê compra cartas automaticamente até atingir pelo menos 17 pontos.
        """
        if self.rodada_encerrada:
            return

        while self.crupie.deve_comprar():
            self.crupie.comprar(self.baralho, self.contador_hilo)

        self.rodada_encerrada = True

    def resultado(self) -> str:
        """
        Determina o resultado final da rodada.

        Retorna:
        ----------
        str
            Mensagem indicando o vencedor ou empate.
        """
        total_jogador = self.jogador.mao.melhor_valor()
        total_crupie = self.crupie.mao.melhor_valor()

        if total_jogador > 21:
            return "Jogador estourou. Crupiê vence."
        if total_crupie > 21:
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
        """
        Retorna uma representação textual do estado atual do jogo.

        Parâmetros:
        ----------
        esconder_primeira_carta_crupie : bool
            Define se a primeira carta do crupiê será ocultada.

        Retorna:
        ----------
        str
            Texto formatado com o estado atual da rodada.
        """
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

        return (
            f"================ BLACKJACK ================\n\n"
            f"Jogador:\n"
            f"  Cartas: {cartas_jogador}\n"
            f"  Total : {self.jogador.mao.melhor_valor()}\n\n"
            f"Crupiê:\n"
            f"  Cartas: {cartas_crupie}\n"
            f"  Total : {total_crupie}\n\n"
            f"{resumo}\n"
        )

    def __str__(self) -> str:
        """
        Retorna um resumo rápido do estado do jogo.

        Inclui:
        - Quantidade de cartas restantes no baralho
        - Contagem Hi-Lo atual

        Retorna:
        ----------
        str
            String resumida do estado do jogo.
        """
        cartas_restantes = self.baralho.cartas_restantes()
        contagem = self.contador_hilo.contagem_atual

        return (
            f"Baralho: {cartas_restantes} cartas restantes\n"
            f"Contagem Hi-Lo: {contagem}"
        )