from Baralho import Baralho
from Carta import Carta
from Mao import Mao
from ContadorHilo import ContadorHilo

# Classe jogador: fundamental para definir conceitos e ações sobre o jogador
class Jogador:
    """
    Representa um jogador no jogo de Blackjack.

    Um jogador possui um nome e uma mão de cartas, podendo realizar
    ações como comprar cartas e limpar sua mão ao final de uma rodada.

    Esta classe serve como base para outros tipos de jogadores,
    como o Crupiê, permitindo reutilização de código e extensão
    de comportamento.

    Atributos:
    ----------
    nome : str
        Nome do jogador.
    mao : Mao
        Objeto que representa a mão de cartas do jogador.

    Métodos:
    ----------
    comprar(baralho, contador_hilo) -> Carta
        Compra uma carta do baralho, adiciona à mão e atualiza o contador Hi-Lo.

    limpar_mao()
        Remove todas as cartas da mão do jogador.
    """

    def __init__(self, nome: str):
        """
        Inicializa um jogador com um nome e uma mão vazia.

        Parâmetros:
        ----------
        nome : str
            Nome do jogador.
        """
        self.nome = nome
        self.mao = Mao(nome)

    def comprar(self, baralho: Baralho, contador_hilo: ContadorHilo) -> Carta:
        """
        Compra uma carta do baralho.

        A carta comprada é:
        - Removida do baralho
        - Adicionada à mão do jogador
        - Utilizada para atualizar o contador Hi-Lo

        Parâmetros:
        ----------
        baralho : Baralho
            O baralho de onde a carta será comprada.
        contador_hilo : ContadorHilo
            Sistema de contagem de cartas que será atualizado.

        Retorna:
        ----------
        Carta
            A carta que foi comprada.
        """
        carta = baralho.comprar_carta()
        self.mao.adicionar_carta(carta)
        contador_hilo.atualizar(carta)
        return carta

    def limpar_mao(self):
        """
        Limpa a mão do jogador.

        Remove todas as cartas, geralmente utilizado ao final de uma rodada.
        """
        self.mao.limpar()

    def __str__(self):
        """
        Retorna uma representação textual do estado atual do jogador.

        Inclui:
        - Nome do jogador
        - Cartas na mão
        - Valor total da mão

        Retorna:
        ----------
        str
            String formatada com as informações do jogador.
        """
        return (f"{self.nome} | "
                f"Mão: {self.mao.cartas} | "
                f"Valor: {self.mao.melhor_valor()}")