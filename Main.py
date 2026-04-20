from JogoBlackjack import JogoBlackjack


def main():

    try:
        jogo = JogoBlackjack(quantidade_baralhos=1)

        while True:  # LOOP INFINITO DO JOGO

            jogo.iniciar_rodada()

            # estado inicial da rodada
            print("Estado inicial:")
            print(jogo.obter_estado_textual())

            # turno do jogador
            while not jogo.rodada_encerrada:

                acao = input("\nAção (hit / stand / sair): ").strip().lower()

                if acao == "hit":
                    print("\nJogador compra uma carta...\n")
                    jogo.jogador_compra()
                    print(jogo.obter_estado_textual())

                elif acao == "stand":
                    print("\nJogador decide parar...\n")
                    jogo.jogador_para()

                elif acao == "sair":
                    print("\nEncerrando o jogo...")
                    return

                else:
                    print("Comando inválido. Use: hit, stand ou sair.\n")

            # fim da rodada
            print("\nRESULTADO\n")
            print(jogo.obter_estado_textual(esconder_primeira_carta_crupie=False))
            print(jogo.resultado())

            input("Pressione ENTER para próxima rodada...")

    except Exception as e:
        print("Erro durante execução:")
        print(e)


if __name__ == "__main__":
    main()
