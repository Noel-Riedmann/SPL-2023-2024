import random

playerNumber = 0
computerNumber = 0

for i in range(6):
    playerNumber += random.randint(1, 6)
    computerNumber += random.randint(1, 6)

print("Player:", playerNumber, "Computer:", computerNumber)

if playerNumber > computerNumber:
    print("Player won!")

elif playerNumber < computerNumber:
    print("Computer won!")

elif playerNumber == computerNumber:
    print("Draw!")
