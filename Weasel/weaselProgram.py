# Inplementação em Python do "Weasel Program" de Richard Dawkin
# Ilustra o poder de seleção cumulativa versus uma perquisa complemante aleatória
# Esta versão permite que todas as posições mudem a cada geração,
# o que significa que letras corretas na geração anterior podem mudar na geração seguinte

# Inicializações

import random # Biblioteca que gera números aleatórios
goal = list(input('ENTRE COM A PALAVARA A SER GERADA: ').upper())   # Recebe uma string via input,
                                                                    # deixa-a toda em caixa alta e cria converte-a ao tipo lista
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "        # Alfabeto com todos os símbolos possíveis (letras em caixa alta + espaço em branco)
nChildren = 100                                # Número de filhos por geração
mutRate = 0.1                                 # Taxa de mutação: probabilidade que uma letra vai mudar
best_offspring = []                             # Variável contendo os melhores filhos de cada geração
                                                # Contém uma lista vazia quando entra no laço pela primeira vez

# Constroi uma string aleatória com o mesmo tamanho da nossa string inicial
parent = []
for i in range(len(goal)):
    parent.append(random.choice(alphabet))

# Loop Principal: constrói vários filhos com mutação, seleciona os melhores para a próxima geração, para quando o 
# um dos filhos tem a string objetivo
gen = 0 # variável que possui o valor da geração

while best_offspring != goal: # enquanto o melhor filho for diferente do objetivo, faça:

    gen = gen + 1 # Aumenta o número da geração

    # Mantém controle do número de mutações boas, ruins e indiferentes que aparecem nessa geração
    nGood = nBad = nNeutral = nMutation = 0.0

    # Mantém o controle do número de filhos da geração atual que são iguais aos pais
    nSame = nChildren

    # Contrói todos os lilhos da geração, que podem ou não conter mutação
    kids = []
    for i in range(nChildren): # Para cada número i em 0 até nChildren faça: 

        # Copia o conteúdo de um pai para um filho
        kid = parent[:]

        # Passa para cada posição da palavra filha abrindo assim a possibilidade de mutação
        kidChanged = False # Valor booleano que diz se uma palavra filha gerada nessa geração mudou ou não com relação ao pai
                            # ou seja, houve mutação

        for pos in range(len(kid)): # Para cada numero (pos) de 0 até (tamanho do filho gerado) faça:

            # Deixa o filho sofrer mutação com a probabilidate (em porcentagem) mutRate
            if random.random() < mutRate: # Se um número aleatório for menor que a taxa de mutação faça:

                kidChanged = True # Sinaliza que houve mutação no filho
                nMutation += 1 # Adiciona mais um ao contador de filhos com mutação

                # Escolhe aleatóriamente um novo símbolo do alfabeto que é diferente do símbolo atual na posição
                oldSymbol = parent[pos] # Variável recebe o símbolo antigo
                possNewSymb = set(alphabet) - set(oldSymbol) # Cria uma lista com todos os possíveis novos símbolos
                newSymbol = random.choice(list(possNewSymb)) # Variável recebe o novo símbolo

                # Muda o filho
                kid[pos] = newSymbol # Filho na posição pos recebe o novo símbolo

                # Checa se a mutação foi benéfica, maléfica ou neutra e incrementa o respectivo contador
                if oldSymbol == goal[pos]:               # Uma letra correta foi alterada: mutação maléfica
                    nBad += 1
                elif newSymbol == goal[pos]:             # Uma letra incorreta foi alterada para uma correta: mutação benéfica
                    nGood += 1
                else:                                           # Uma letra incorreta foi alterada para outra letra incorreta: mutação neutra
                    nNeutral += 1

        # If kid was mutated, then it no longer looks like its parent
        if kidChanged:
            nSame -= 1

        # Add (possibly) mutated kid to list of current kids
        kids.append(kid)


    # Find most fit offspring (= string most similar to goal)
    smallest_dif = len(goal) + 1
    for kid in kids:

        # Find number of positions that differ between kid and goal
        dif = 0.0
        for pos in range(len(goal)):
            if kid[pos] != goal[pos]:
                dif = dif + 1

        # Keep best kid found so far
        if dif < smallest_dif:
            smallest_dif = dif
            best_offspring = kid

    # Use best offspring as starting point for next round of mutation
    parent = best_offspring

    # Print progress
    fitness = (len(goal)-smallest_dif)/len(goal)            # Fitness of most fit individual
    ben_frac = nGood/nMutation
    detr_frac = nBad/nMutation
    neu_frac = nNeutral/nMutation
    result_string = ""
    for pos in range(len(goal)):
        if best_offspring[pos] == goal[pos]:
            result_string += best_offspring[pos]
        else:
            result_string += best_offspring[pos].lower()
    print ("%s     ** Gen: %4d   Dif: %3d   Fit: %.4f   Bene: %.4f  Detr: %.4f  Neu: %.4f   Unchanged: %3d" % (result_string, gen, smallest_dif, fitness, ben_frac, detr_frac, neu_frac, nSame))