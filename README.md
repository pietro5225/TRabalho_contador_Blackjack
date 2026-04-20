# Blackjack com Análise Probabilística (Hi-Lo + Probabilidade Real)

## Descrição do Projeto

Este projeto implementa o jogo de Blackjack (21) em Python utilizando Programação Orientada a Objetos (POO), incorporando:

- Sistema completo de jogo (jogador vs crupiê)
- Contagem de cartas com método Hi-Lo
- Cálculo de probabilidades reais baseadas no baralho atual
- Comparação entre estimativas probabilísticas e valores reais

O objetivo é unir simulação de jogo com análise matemática e estatística, permitindo avaliar estratégias e comportamento probabilístico em tempo real.


## Objetivos

- Implementar um sistema modular de Blackjack  
- Aplicar conceitos de POO (encapsulamento, herança)  
- Simular contagem de cartas (Hi-Lo)  
- Calcular probabilidades reais a partir do estado do baralho  
- Comparar:
  - Probabilidade empírica (Hi-Lo)
  - Probabilidade real (cálculo direto)


## Conceitos Utilizados

### Blackjack
- Objetivo: atingir 21 pontos ou o mais próximo sem ultrapassar  
- Ás pode valer 1 ou 11  
- Figuras valem 10  

### Método Hi-Lo

Sistema de contagem onde:
- Cartas baixas (2–6): +1  
- Cartas médias (7–9): 0  
- Cartas altas (10–A): -1  

**True Count:**
True Count = Running Count / Número de baralhos restantes

## Estrutura do Projeto

projeto_blackjack/
│
├── Carta.py

├── Baralho.py

├── Mao.py

├── Jogador.py

├── ContadorHilo.py

├── MotorProbabilidade.py

├── JogoBlackjack.py

└── main.py


## Arquitetura das Classes

### Carta
Representa uma carta individual.

Responsabilidades:
- Valor no Blackjack  
- Valor no Hi-Lo  


### Baralho
Representa um ou mais decks.

Funções:
- Criar cartas  
- Embaralhar  
- Comprar carta  


### Mao
Representa a mão de um jogador.

Funções:
- Calcular valor total (tratamento de Ás)  
- Verificar Blackjack  


### Jogador
Classe base para jogadores.


### Crupiê (Herança)
- Herda de Jogador  
- Regra: compra até atingir 17  


### ContadorHiLo

Responsável pela contagem de cartas.

Calcula:
- Running Count  
- True Count  
- Vantagem estimada  
- Probabilidade de carta alta  


### MotorProbabilidade

Calcula probabilidades reais com base no baralho atual:

#### Probabilidade de perder (estourar)
P = cartas que ultrapassam 21 / total de cartas

#### Probabilidade de carta alta
P = cartas ≥ 10 / total de cartas

#### Probabilidade por carta
Distribuição completa das cartas restantes

#### Comparação com Hi-Lo
Erro = Probabilidade real - Probabilidade estimada


### JogoBlackjack

Controla o fluxo do jogo:

- Início da rodada  
- Turno do jogador  
- Turno do crupiê  
- Resultado final  
- Estado textual do jogo  

## Funcionalidades Implementadas

- Sistema completo de jogo  
- Múltiplos baralhos  
- Contagem Hi-Lo dinâmica  
- Probabilidade real baseada no estado atual  
- Relatórios estratégicos  
- Comparação entre modelo empírico e real  

## Exemplo de Saída
--- Análise Hi-Lo ---
Contagem Corrente : 5
True Count : 2.50
Vantagem Estimada : 0.75%
Prob. Carta Alta : 42.3%


## Como Executar

1. Clone o repositório:
git clone https://github.com/seu-usuario/blackjack-poo.git

2. Acesse a pasta:
cd blackjack-poo

Execute:
python main.py

## Autores:
Joaquim Simoes
Mateus Almeida
Pietro Grizendi
Rafael Barbosa
