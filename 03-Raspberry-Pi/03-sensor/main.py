import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the encoder
CLK_PIN = 17
DT_PIN = 27
SW_PIN = 22  # Optional, for the switch

# Set GPIO mode and define pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Optional, enable internal pull-up resistor for the switch

# Variables to store the current and previous state of the encoder
encoderValue = 0
encoderLastValue = 0

try:
    while True:
        # Read the state of the encoder pins
        CLK_state = GPIO.input(CLK_PIN)
        DT_state = GPIO.input(DT_PIN)
        SW_state = GPIO.input(SW_PIN)

        # Check for rotation
        if CLK_state != DT_state:
            if CLK_state == 1:
                encoderValue += 1
            else:
                encoderValue -= 1
            print(encoderValue)

        # Check for switch press
        if SW_state == 0:
            print("Switch pressed!")
            # Add your switch press handling code here
            time.sleep(0.5)  # Optional debounce delay

        # Small delay to improve responsiveness
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting program")
finally:
    GPIO.cleanup()
