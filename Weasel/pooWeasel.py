from tkinter import *
import random  # Biblioteca que gera números aleatórios


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"


#root = Tk()
#Application(root)
#root.mainloop()




class WeaselAlgorithm:
    def __init__(self, goal, children, mutation):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
        self.numChild = children
        self.mutRate = mutation
        self.bestKid = []
        self.parent = []
        self.goal = goal
        self.gen = 0
        self.good = 0.0
        self.bad = 0.0
        self.neutral = 0.0
        self.mutation = 0.0
        self.same = 0
        self.exit = []

    def process(self):
        for i in range(len(self.goal)):
            self.parent.append(random.choice(self.alphabet))
            
        while self.goal != self.bestKid:
            self.generateChildren(self.bestKid)

        self.printExit()

    def resetStatus(self):
        self.good = 0.0
        self.bad = 0.0
        self.neutral = 0.0
        self.mutation = 0.0
        self.same = 0.0

    def findBestKid(self, kids):

        smallestDiff = len(self.goal)+1

        for kid in kids:

            dif = 0

            for i in range(len(self.goal)):
                if kid[i] != self.goal[i]:
                    dif += 1

            if dif < smallestDiff:
                smallestDiff = dif
                self.parent = kid

        self.generateExit(smallestDiff)

    def generateExit(self, smallestDiff):
        fitness = (len(self.goal)-smallestDiff)/len(self.goal)
        good = self.good/self.mutation
        bad = self.bad/self.mutation
        neutral = self.neutral/self.mutation
        ex = ""

        for i in range(len(self.goal)):
            if self.bestKid[i] == self.goal[i]:
                ex += self.bestKid[i]
            else:
                ex += self.bestKid[i]

            ex = "\n-------Geração: %4d   : %s -------\nTaxas de mutação dos filhos:\n Elementos Diferentes: %3d   Fit: %.4f   Boa: %.4f  Ruim: %.4f  Neutra: %.4f  Indiferente: %3d" % (
                self.gen, ex, smallestDiff, fitness, self.good, self.bad, self.neutral, self.same)

            self.exit.append(ex)
        
        self.resetStatus()
    
    def printExit(self):
        for e in self.exit:
            print(e)

    def generateChildren(self, parent):
        self.gen += self.gen

        kids = []

        for i in range(self.numChild):

            kid = parent[:]
            kidChanged = False

            for p in range(len(kid)):

                if random.random() < self.mutRate:

                    kidChanged = True
                    self.mutation += 1

                    oldSymb = parent[p]
                    possNewSymb = set(self.alphabet) - set(oldSymb)
                    newSymb = random.choice(list(possNewSymb))
                    kid[p] = newSymb

                    if oldSymb == self.goal[p]:
                        self.bad += 1
                    elif newSymb == self.goal[p]:
                        self.good += 1
                    else:
                        self.neutral += 1

                if kidChanged:
                    self.same -= 1

                kids.append(kid)

        self.findBestKid(kids)


entry = list(input('ENTRE COM A STRING A SER GERADA: ').upper())

weasel = WeaselAlgorithm(entry, 100, 0.1)

weasel.process()