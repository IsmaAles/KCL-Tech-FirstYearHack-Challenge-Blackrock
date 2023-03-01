import networkx as nx
import matplotlib.pyplot as plt
#This class handling numbers and its factors.
class Number:

    def __init__(self, startNumber):
        self.startNumber = startNumber
        self.exponent = 1
        self.primeFactors = self.getPrimeFactors(self.startNumber)

    def getPrimeFactors(self, num):
        i = 2
        factors = []
        while i**2 <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return factors 
    
    def isDivisible(self, divisor):
        counter = self.exponent
        for i in range(counter, 0, -1):
            flag = False
            for n in self.primeFactors:
                if divisor % n == 0:
                    divisor /= n
                    flag = True
                    if divisor == 1:
                        return True
            if flag == False:
                return False
        return False
            
#This classs represents each from the Blackrock challenge
class Bot:

    def __init__(self, name, initialSecurities):
        self.name = name
        self.initialSecurities = initialSecurities
        self.rule = []
        self.tradeno = 0

    def trade(self):
        for security in self.initialSecurities:
            security.exponent *= 2
            if security.isDivisible(self.rule[0]):
                self.rule[1].initialSecurities.append(security)
            else:
                self.rule[2].initialSecurities.append(security)
            self.tradeno += 1
        self.initialSecurities  = []
        
    def addRule(self, rule):
        self.rule = rule

#Creating the bots
botAda = Bot("Ada", [Number(3), Number(4), Number(6)])
botLovelace = Bot("Lovelace", [Number(8), Number(2)])
botAlan = Bot("Alan", [Number(5)])
botTuring = Bot("Turing", [Number(5), Number(7), Number(9)])
botAnna = Bot("Anna", [Number(7), Number(8), Number(9)])

#Linking the rules to the bots
botAda.addRule([4, botTuring, botAlan])
botLovelace.addRule([5, botAda, botTuring])
botAlan.addRule([3, botAnna, botLovelace])
botTuring.addRule([6, botLovelace, botAnna])
botAnna.addRule([2, botAlan, botAda])

#Creating a list with bots in order to iterate
botList =  [botAda, botLovelace, botAlan, botTuring, botAnna]

#Trade iteration
for i in range(5000):
    for bot in botList:
        bot.trade()


DG = nx.DiGraph()

#Print the tradenumbers and add graph edges
for bot in sorted(botList, key = lambda x: x.tradeno, reverse = True):
    print("Bot " + bot.name + ": " + str(bot.tradeno))
    DG.add_edges_from([(bot.name, bot.rule[1].name), (bot.name, bot.rule[2].name)])


options = {
    'node_color': 'white',
    'node_size': 5000,
    'width': 2
}

nx.draw(DG, with_labels=True, font_weight='bold', **options)
plt.show()  