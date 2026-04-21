from JogoBlackjack import JogoBlackjack 

quantidade_baralhos=10
continuar_jogo=True
jogo=JogoBlackjack(quantidade_baralhos)


while(continuar_jogo):

    jogo.iniciar_rodada()
    print(jogo.obter_estado_textual())

    while not jogo.rodada_encerrada:
        escolha=input("Digite 'c' para comprar ou 'p' para parar ").strip().lower()

        if escolha== 'c':
            jogo.jogador_compra()
            print(jogo.obter_estado_textual())
    
        elif escolha=='p':
            jogo.jogador_para()

        else:
            print("Digite uma letra valida, 'c' para comprar ou 'p' para parar")

    print(jogo.obter_estado_textual(False))  # revela carta do crupiê
    print(jogo.resultado())

    resposta = input("Quer jogar de novo? (s/n): ").strip().lower()
    while(resposta!='s'and resposta!='n'):
        resposta=input("Digite 's' ou 'n' continuar ou para sair")
    if resposta=='s':
        continuar_jogo=True
    else:
        continuar_jogo=False
        print("Obrigado por jogar!")

    



    

