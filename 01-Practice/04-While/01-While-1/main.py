import random

total = 0
randomNumber = 0

while randomNumber != 15 and randomNumber != 25:
    randomNumber = random.randint(10, 30)
    total += randomNumber

print('Total:', total, 'Last number:',randomNumber)

