import random

randomNumber = random.randint(0, 100)

if randomNumber < 20:
    print('Mini: ', randomNumber)
elif randomNumber < 50 & randomNumber >= 20:
    print('Medium: ', randomNumber)
else:
    print('Large: ', randomNumber)


