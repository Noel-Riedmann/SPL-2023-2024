import random

randomNumberOne = random.randint(0, 100)
randomNumberTwo = random.randint(0, 100)
print('Number 1:', randomNumberOne, 'Number 2:',randomNumberTwo)

if randomNumberOne < randomNumberTwo & randomNumberOne < 50:
    print('Zahl 1 ist kleiner als Zahl 2 und Mini')
elif randomNumberOne < 30 | randomNumberTwo < 30:
    print('Eine der beiden ist kleiner als 30')
elif randomNumberOne < 50 & randomNumberTwo != 50:
    print('Erste Zahl klein, zweite kein 50iger')
