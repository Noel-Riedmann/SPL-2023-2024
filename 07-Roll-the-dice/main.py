import random

playerNumber = 0
computerNumber = 0

for i in range(6):
    playerNumber += random.randint(1, 5) + 1
    computerNumber += random.randint(1, 5) + 1

print("Player:", playerNumber, "Computer:", computerNumber)

if playerNumber > computerNumber:
    print("Player won!")

elif playerNumber < computerNumber:
    print("Computer won!")

elif playerNumber == computerNumber:
    print("Draw!")
