from Jogador import Jogador

class Crupie(Jogador):
    """
    Representa o crupiê (dealer) no jogo de Blackjack.

    O crupiê é um tipo especial de jogador que segue regras fixas
    definidas pelo jogo, ao contrário do jogador humano que pode
    tomar decisões livres.

    Regras padrão implementadas:
    - O crupiê deve comprar cartas enquanto o valor da mão for menor que 17.
    - Ao atingir 17 ou mais, ele deve parar.

    Herda da classe Jogador, reutilizando atributos como:
    - nome
    - mao (mão de cartas)
    - métodos de compra e manipulação de cartas

    Métodos:
    ----------
    deve_comprar() -> bool
        Retorna True se o crupiê deve comprar mais uma carta,
        com base no valor atual da mão.
    """

    def __init__(self):
        """
        Inicializa o crupiê com nome padrão 'Crupiê'.
        """
        super().__init__("Crupiê")

    def deve_comprar(self) -> bool:
        """
        Determina se o crupiê deve comprar mais uma carta.

        Retorna:
        ----------
        bool
            True se o valor da mão for menor que 17,
            False caso contrário.
        """
        return self.mao.melhor_valor() < 17

    def __str__(self):
        """
        Retorna uma representação textual do estado atual do crupiê.

        Inclui:
        - Nome
        - Cartas na mão
        - Valor total da mão

        Retorna:
        ----------
        str
            String formatada com as informações do crupiê.
        """
        return (f"{self.nome} | "
                f"Mão: {self.mao.cartas} | "
                f"Valor: {self.mao.melhor_valor()}")