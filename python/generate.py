import random
cards = ["jack", "queen", "king"]

random.shuffle(cards)                   #embaralhar
for card in cards:
    print(card)



"""import random

number = random.randint(1, 10)      #escolhe um numero entre 1 e 10
print(number)


from random import choice

coin = choice(["heads", "tails"])           #to flip a coin
print(coin)



import random     #importa tudo da funcao random

coin = random.choice(["heads", "tails"])           #to flip a coin
print(coin)
"""