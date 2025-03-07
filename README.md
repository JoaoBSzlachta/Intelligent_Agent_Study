# Intelligent_Agent_Study
Estudo de agentes inteligentes através do jogo de cartas Paciência (Solitaire)

### Observação
Por conta da complexidade tanto técnica quanto contextual, foi construído apenas o código dos agentes reativo simples e reativo com estado interno. 
Paciência é um jogo, o qual apresenta algumas nuancias dificeis de serem abstraidas para o contexto de agentes inteligentes. 
Uma vez que cada pequeno detalhe nas regras como lembrar a última carta saquada ou reorganizar as colunas podem pertencer tanto a um agente mais simples como reativo com estado interno quanto a um mais complexo quanto o baseado em objetivo.

A seguir são explicados os limites pensados para cada agente bem como seu ambiente de trabalho e como o jogo foi montado para que o código (o agente) pudesse jogar sozinho. 

## PEAS

|Tipo do Agente| Medida de Desempenho                  | Ambiente            | Atuadores                              | Sensores                                                           |
| --- |---------------------------------------|---------------------|----------------------------------------|--------------------------------------------------------------------|
|Jogador de Paciência| Terminar o jogo respeitando as regras | Tabuleiro com carta | Atualizar estado da carta/ Mover carta | Verificiar valor/ Verificar cor/ Verificar naipe/ Varificar estado |

| Ambiente de Tarefa   | Observável   | Agentes | Determinístico | Episódico | Estático | Discreto |
|----------------------|--------------|---------|----------------|-----------|----------|----------|
| Tabuleiro com cartas | Parcialmente | Único   | Estocástico    | Episódico | Estático | Discreto |

## Set Up
O baralho (deck) originalmente é composto por 52 cartas divididas entre vermelhas e pretas, e em 4 naipes diferentes (copas, ouro, paus e espadas). Cada carta é um array que possui 4 valores (símbolo, naipe, cor, estado) e o deck é um array de cartas. Os símbolos das cartas variam de 'A' a 'K' e o estado representa se a carta está com o conteúdo para baixo ou para cima, facilitando a ideia de ver as cartas disponíveis.

As colunas são montadas da forma que o último elemento do array representa a carta virada para cima no final da coluna. Ao todo há 6 colunas mais 4 arrays que representam os decks de naipes. Pois o objetivo do jogo é manipular as posições das cartas nas colunas e separar cada naipe em um monte de cartas diferente, começando do 'A' e evoluir até o 'K'.

O array rejected_deck é onde o agente guarda as cartas que ele não conseguiu posicionar. A partir do Agente Reativo com Estado Interno, o jogador poderá o usar as cartas do rejected_deck para tentar posicioná-las novamente, uma vez que o agente pode contar quantas vez ele já tentou usar as cartas nas colunas e não obteve sucesso. Caso não houvesse essa contagem (memória), o agente poderia entrar em um loop de tentativas fracassadas.

É válido ressaltar que o agente é responsável apenas por jogar. Por isso foram criadas outras funções pertencentes à classe Cards que embaralham o deck e preparam a mesa (board) para o agente poder iniciar.

## Agente Reativo Simples

O agente realiza as seguintes ações:

  - retira a última carta do array deck;
  - visualiza seu valor, naipe e cor;
  - define o estado como 'UP';
  - verifica se a carta encaixa em um dos decks de naipe*,
    - se sim: coloca a carta no array (append),
    - se não: verifica se esta carta encaixa no final de uma das colunas**,
      - se sim: coloca a carta no array (append),
      - se não: descarta a carta.

*A carta precisa ser de mesmo naipe seguindo a ordem crescente dos valores (de 'A' a 'K').

**A carta precisa ser de cor oposta e diretamente a próxima na lista de hierarquia em ordem descrescente dos valores (de 'K' a 'A').

## Agente Reativo com Estado Interno

O agente realiza a mesma ordem de ações que Agente Reativo Simples, mas ele consegue reaproveitar as cartas descartadas.

Após tentar posicionar todas as cartas do deck, o agente pega o rejected_deck com todas as cartas que não foram postas, e utiliza como o novo deck e tenta posicionar as cartas restantes.

Caso ele não consiga posicionar uma única carta, ele começa a contar as tentativas e tenta novamente posicionar as cartas do rejected_deck. Passando de 2 tentativas, o agente afirma que não possível terminar o jogo.

Caso ele consiga colocar ao menos uma carta, o agente continua tentando pôr as cartas do rejected_deck na mesa, até que não consiga pôr mais nenhuma.

## Agentes Baseado em Objetivo e Baseado em Utilidade
Idealizando a implementação desses agentes para o jogo de paciência pode-se pensar em fazer o jogador verificar as sub-colunas (cartas viradas para cima em uma coluna) e mover elas por completo para a última posição de outra coluna para liberar as cartas ainda não viradas que estão embaixo das subcolunas.

## Agente Baseado em Utilidade
Esse jogador poderá verificar quanto da subcoluna ele gostaria de mover para outra coluna, como por exemplo, dado a subcoluna:

- 8ouros - 7paus - 6ouros - 5espadas.

O jogoador poderia decidir mover apenas (- 6ouros - 5espadas) para poder liberar a carta (7paus) para ser posta nos deck do naipe correspondente ou em outra coluna para poder utilizar da carta sacada do deck.
