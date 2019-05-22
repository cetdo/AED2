# Implementação em Python do "Weasel Program" de Richard Dawkin
# Ilustra o poder de seleção cumulativa versus uma perquisa complemante aleatória
# Esta versão permite que todas as posições mudem a cada geração,
# o que significa que letras corretas na geração anterior podem mudar na geração seguinte

# Inicializações

import random  # Biblioteca que gera números aleatórios
# Recebe uma string via input,
goal = list(input('ENTRE COM A PALAVARA A SER GERADA: ').upper())
# deixa-a toda em caixa alta e cria converte-a ao tipo lista
# Alfabeto com todos os símbolos possíveis (letras em caixa alta + espaço em branco)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 " # Alfabeto com as letras + espaço em branco para gerar a String
nChildren = 100                                 # Número de filhos por geração
# Taxa de mutação: probabilidade que uma letra vai mudar 0 < mutRate =< 1
mutRate = 0.10
# Variável contendo os melhores filhos de cada geração
bestOffspring = []
# Contém uma lista vazia quando entra no laço pela primeira vez

# Constroi uma string aleatória com o mesmo tamanho da nossa string inicial
parent = []

for i in range(len(goal)):
    parent.append(random.choice(alphabet))

# Loop Principal: constrói vários filhos com mutação, seleciona os melhores para a próxima geração, para quando o
# um dos filhos tem a string objetivo
gen = 0  # variável que possui o valor da geração

# enquanto o melhor filho for diferente do objetivo, faça:
while bestOffspring != goal:

    gen = gen + 1  # Aumenta o número da geração

    # Mantém controle do número de mutações boas, ruins e indiferentes que aparecem nessa geração
    nGood = nBad = nNeutral = nMutation = 0.0

    # Mantém o controle do número de filhos da geração atual que são iguais aos pais
    nSame = nChildren

    # Contrói todos os filhos da geração, que podem ou não conter mutação
    kids = []

    for i in range(nChildren):  # Para cada número i em 0 até nChildren faça:

        # Copia o conteúdo de um pai para um filho
        kid = parent[:]

        # Passa para cada posição da palavra filha abrindo assim a possibilidade de mutação
        kidChanged = False  # Valor booleano que diz se uma palavra filha gerada nessa geração mudou ou não com relação ao pai
        # ou seja, houve mutação

        # Para cada numero (pos) de 0 até (tamanho do filho gerado) faça:
        for pos in range(len(kid)):

            # Deixa o filho sofrer mutação com a probabilidate (em porcentagem) mutRate
            # Se um número aleatório for menor que a taxa de mutação faça:
            if random.random() < mutRate:

                kidChanged = True  # Sinaliza que houve mutação no filho
                nMutation += 1  # Adiciona mais um ao contador de filhos com mutação

                # Escolhe aleatóriamente um novo símbolo do alfabeto que é diferente do símbolo atual na posição
                oldSymbol = parent[pos]  # Variável recebe o símbolo antigo
                # Cria uma lista com todos os possíveis novos símbolos
                possNewSymb = set(alphabet) - set(oldSymbol)
                # Variável recebe o novo símbolo
                newSymbol = random.choice(list(possNewSymb))

                # Muda o filho
                # Filho na posição pos recebe o novo símbolo
                kid[pos] = newSymbol

                # Checa se a mutação foi benéfica, maléfica ou neutra e incrementa o respectivo contador
                # Uma letra correta foi alterada: mutação maléfica
                if oldSymbol == goal[pos]:
                    nBad += 1
                # Uma letra incorreta foi alterada para uma correta: mutação benéfica
                elif newSymbol == goal[pos]:
                    nGood += 1
                else:                                    # Uma letra incorreta foi alterada para outra letra incorreta: mutação neutra
                    nNeutral += 1

        # Se um filho sofre mutação, ele não é mais igual aos pais
        if kidChanged:
            nSame -= 1
            
        # Adiciona o filho no vetor de filhos
        kids.append(kid)

    # Encontra o filho que mais se parece com o objetivo
    smallestDiff = len(goal) + 1 # a variável é inicializada com o tamanho do objetivo + 1
                                 # simbolizando o menor maior número de diferenças

    # Para cada filho no array de filhos, faça:
    for kid in kids:

        # Encontre a quantidade de diferenças entre o filho e o pai
        dif = 0 # inicizaliza o contador de diferenças
        for pos in range(len(goal)): # para indice (pos) de 1 até o tamanho do objetivo -1 , faça:
            if kid[pos] != goal[pos]: # se o elemento do filho no índice [pos] é diferente do elemento do objetivo no índice [pos]: 
                dif = dif + 1 # aumenta o número de diferenças em 1

        
        if dif < smallestDiff: # se o número de diferenças do filho atual for menor que o menor número de diferenças até agora
            smallestDiff = dif # Menor numero de diferenças recebe o numero de diferenças do filho atual
            bestOffspring = kid # Melhor filho recebe o filho atual

    # Usa o melhor filho como ponto de partida para a próxima geração
    parent = bestOffspring

    # Imprime o processo
    fitness = (len(goal)-smallestDiff)/len(goal) # Fitness é o indivíduo mais semelhança ao objetivo
    goodFraction = nGood/nMutation # Fração boa recebe a quantidade de indivíduos com mutação boa sobre o total de mutações
    badFraction = nBad/nMutation # Fração ruim recebe a quantidade de mutações ruins sobre o total de mutações
    neutralFraction = nNeutral/nMutation # Fração neutra recebe a quantidade de mutações neutras sobre as mutações totais
    exit = "" # String de saída recebe palavra vazia
    
    for pos in range(len(goal)): # Para cada índoce (pos) de 0 até o tamanho do objetivo, faça:
        if bestOffspring[pos] == goal[pos]: # Se o elemento na posição [pos] do melhor filho for igual ao elemento na posição [pos] do objetivo
            exit += bestOffspring[pos] # Escreva na String de saída o elemento na posição [pos] 
        else: # se não
            exit += bestOffspring[pos].lower() # Escreva na String de saída o elemento do melhor filho posição [pos] em caixa baixa
    print("\n-------Geração: %4d   : %s -------\nTaxas de mutação dos filhos:\n Elementos Diferentes: %3d   Fit: %.4f   Boa: %.4f  Ruim: %.4f  Neutra: %.4f  Indiferente: %3d" %
          (gen, exit, smallestDiff, fitness, goodFraction, badFraction, neutralFraction, nSame)) # Imprime os dados coletados
