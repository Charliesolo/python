from random import choice, randint, shuffle

i=0
while i< 3:
    x = choice([0,1,2,3,4,5,6,7,8,9])
    print(x)
    i += 1

number = randint(1,10)
print(number)

cards = ["jack", "queen", "king", "ace"]
shuffle(cards)
for card in cards:
    print(card)