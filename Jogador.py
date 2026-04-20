import Baralho
import Carta,Mao
#Classe jogador: fundamental para definir conceitos e ações sobre o jogador
class Jogador:
    def _init_(self, nome: str):
        self.nome = nome
        self.mao = Mao(nome)

    def comprar(self, baralho: Baralho, contador_hilo: ContadorHiLo) -> Carta:
        carta = baralho.comprar_carta()
        self.mao.adicionar_carta(carta)
        contador_hilo.atualizar(carta)
        return carta

    def limpar_mao(self):
        self.mao.limpar()

