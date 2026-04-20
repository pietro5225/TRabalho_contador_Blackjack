from JogoBlackjack import JogoBlackjack
def main():
    print("=== TESTE DO JOGO BLACKJACK ===\n")

    try:
        jogo = JogoBlackjack()
    
        # inicia rodada
        jogo.iniciar_rodada()

        print("Estado inicial:")
        print(jogo.obter_estado_textual())

        # jogador compra 1 carta
        print("\nJogador compra uma carta...\n")
        jogo.jogador_compra()

        print(jogo.obter_estado_textual())

        # jogador para
        print("\nJogador decide parar...\n")
        jogo.jogador_para()

        print("\nEstado final:")
        print(jogo.obter_estado_textual(False))

        # resultado final
        print("\nResultado:")
        print(jogo.resultado())

    except Exception as e:
        print("Erro durante execução:")
        print(e)


if __name__ == "__main__":
    main()