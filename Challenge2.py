from math import ceil

#This classs represents each from the Blackrock challenge
class Bot:

    def __init__(self, name, initialSecurities):
        self.name = name
        self.initialSecurities = initialSecurities
        self.rule = []
        self.tradeno = 0

    def trade(self):
        for security in self.initialSecurities:
            value=ceil(((security**2)*0.2))
            if value % self.rule[0] == 0:
                self.rule[1].initialSecurities.append(value)
            else:
                self.rule[2].initialSecurities.append(value)
            self.tradeno += 1
        self.initialSecurities =[]
        
    def addRule(self, rule):
        self.rule = rule


#Creating the bots
botAda = Bot("Ada", [3, 4, 6])
botLovelace = Bot("Lovelace", [8, 2])
botAlan = Bot("Alan", [5])
botTuring = Bot("Turing", [5, 7, 9])
botAnna = Bot("Anna", [7, 8, 9])

#Linking the rules to the bots    
botAda.addRule([4, botTuring, botAlan])
botLovelace.addRule([5, botAda, botTuring])
botAlan.addRule([3, botAnna, botLovelace])
botTuring.addRule([6, botLovelace, botAnna])
botAnna.addRule([2, botAlan, botAda])

#Creating a list with bots in order to iterate
botList = [botAda, botLovelace, botAlan, botTuring, botAnna]

#Trade iteration
for i in range(2):
    for bot in botList:
        bot.trade()

#Print the tradenumbers
for bot in sorted(botList, key = lambda x: x.tradeno, reverse = True):
    print("Bot " + bot.name + ": " + str(bot.tradeno))