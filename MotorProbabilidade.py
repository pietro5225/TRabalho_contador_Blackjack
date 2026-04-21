from ContadorHilo import ContadorHilo
from Carta import Carta

class MotorProbabilidade:
    def __init__(self,baralho,contador_hilo):
        self.baralho=baralho
        self.contador_hilo= contador_hilo
        

    def calcular_probabilidades_reais(self,mao_atual: int)-> float:
        """Calcula a probabilidade de estourar a mão e perder """
        baralho_atual=len(self.baralho.cartas)
        cartas_perde=0
        limite=21-mao_atual  

        for carta in self.baralho.cartas: 
            if carta.valor_blackjack()>limite:
                cartas_perde+=1

        return ((cartas_perde/baralho_atual)*100)
    
    def probabilidade_carta_alta(self)-> float :
        """Calcula a probabilidade de ter cartas altas no baralho """
        baralho_atual=len(self.baralho.cartas)
        cartas_altas=0

        for carta in self.baralho.cartas:
           if int(carta.valor_blackjack())>=10:
               cartas_altas+=1

        return ((cartas_altas/baralho_atual)*100)
    
    def probabilidade_cada_carta(self)-> dict:
        """Calcula a probabilidade de tirar cada uma das cartas no baralho """
        baralho_atual=len(self.baralho.cartas)
        valores=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        probababilidades_por_carta={}
        cont=0

        for valor_alvo in valores:
            encontradas = 0
            for i in range(baralho_atual):
                if (self.baralho.cartas[i].valor==valor_alvo):
                    encontradas+=1
            probababilidades_por_carta[valor_alvo]=((encontradas/baralho_atual)*100)    
        return probababilidades_por_carta
        #Retorna um dicionario com cada probabilidade de tirar cada uma das cartas
    
    def probabilidade_calculada(self)-> float:
        """Calcula a probabilidade de carta alta- a probabilidade contada com o método HiLo """
        return (self.probabilidade_carta_alta()-((self.contador_hilo.probabilidade_empirica_alta(len(self.baralho.cartas)))))
    
    def obter_resumo_probabilidades(self, mao_atual:int )->str:
        """A função que mostra cada uma das probabilidades calculadas na classe """
        chance_estourar=self.calcular_probabilidades_reais(mao_atual)
        chance_alta=self.probabilidade_carta_alta()
        dif_hilo=self.probabilidade_calculada()

        resumo=(
           f"------------------------------\n"
           f"Risco de estourar: {chance_estourar:.1f}%  \n"
           f"Chance de carta alta no baralho: {chance_alta:.1f}% \n"
           f"Sua chance real em comparação com o hilo: {dif_hilo:.2f}% \n"
        )
        return resumo


