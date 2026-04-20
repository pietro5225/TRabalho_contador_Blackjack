import ContadorHilo

class MotorProbabilidade:
    def __init__(self,baralho,contador_hilo):
        self.baralho=baralho
        self.contador_hilo= contador_hilo
        

    def calcular_probabilidades_reais(self,mao_atual):
        baralho_atual=len(self.baralho.cartas)
        cartas_perde=0
        limite=21-mao_atual  

        for carta in self.baralho.cartas: 
            if carta.valor_blackjack()>limite:
                cartas_perde+=1

        return ((cartas_perde/baralho_atual))
    
    def probabilidade_carta_alta(self):
        baralho_atual=len(self.baralho.cartas)
        cartas_altas=0

        for carta in self.baralho.cartas:
           if carta.valor_blackjack()>=10:
               cartas_altas+=1

        return (cartas_altas/baralho_atual)
    
    def probabilidade_cada_carta(self):
        baralho_atual=len(self.baralho.cartas)
        valores=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        probababilidades_por_carta={}
        cont=0

        for valor_alvo in valores:
            encontradas = 0
            for i in range(baralho_atual):
                if (self.baralho.cartas[i].valor==valor_alvo):
                    encontradas+=1
            probababilidades_por_carta[valor_alvo]=(encontradas/baralho_atual)    
        return probababilidades_por_carta
        #Retorna um dicionario com cada probabilidade de tirar cada uma das cartas
    
    def probabilidade_calculada(self):
        return (self.probabilidade_carta_alta()-((self.contador_hilo.probabilidade_empirica_alta(len(self.baralho.cartas)))/100))*100
    
    def relatorio_final(self):
        print(f"A diferença entre a chance real e o método hilo é de {self.probabilidade_calculada():.2f}%")

