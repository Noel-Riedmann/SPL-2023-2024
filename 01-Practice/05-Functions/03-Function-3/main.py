import random

wordArray = ['hello', 'luci', 'joni']


def wordFromArray():
    randomNumber = random.randint(0,2)
    return wordArray[randomNumber]


print(wordFromArray())
