import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

input_value = 'none'

while True:
    if input_value == 'e' or input_value == 'E':
        GPIO.output(17, True)
        print("LED turned on")
        input_value = 'none'

    elif input_value == 'a' or input_value == 'A':
        GPIO.output(17, False)
        print('LED turned off')
        input_value = 'none'

    elif input_value == 'none':
        input_value = input('Enter "e" for on and "a" for off: ')
