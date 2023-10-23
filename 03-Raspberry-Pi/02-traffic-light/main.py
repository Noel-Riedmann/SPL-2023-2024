import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # red
GPIO.setup(27, GPIO.OUT)  # green

input_value = 'none'
light = 'red'

while True:
    if input_value == '':
        if light == 'red':
            GPIO.output(17, False)
            GPIO.output(27, True)
            light = 'green'
        elif light == 'green':
            GPIO.output(17, True)
            GPIO.output(27, False)
            light = 'red'
        print("Traffic Light is now", light)
        input_value = 'none'

    elif input_value == 'none':
        input_value = input('Enter enter to switch: ')
