isRunning = True
total = 0

while isRunning:
    choice = int(input('Enter 1 to deposit or 2 to withdraw or 3 to see your balance or 4 to exit: '))

    if choice == 4:
        isRunning = False
    elif choice == 1:
        number = int(input('Enter a number to deposit: '))
        total += number
        print('Total:', total)
    elif choice == 2:
        number = int(input('Enter a number to withdraw: '))
        total -= number
        print('Total:', total)
    elif choice == 3:
        print('Total:', total)
    else:
        print('Invalid choice. Please enter 1, 2, or 4 to exit.')
