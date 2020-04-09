import RPi.GPIO as GPIO

def setup():
    print("Setup...")

    # Use BCM mode
    GPIO.setmode(GPIO.BCM)

    # Setup input pins
    GPIO.setup(16, GPIO.IN)
    # TODO #2 Setup other buttons/pins
    GPIO.setup(17, GPIO.IN)

    # Setup output pins
    GPIO.setup(21, GPIO.OUT)

    print("Setup completed!")

def main():
    print("Run...")

    # Register event listeners for GPIOs
    GPIO.add_event_detect(16, GPIO.FALLING, callback=isr_falling, bouncetime=300)

    # Wait endlessly (17 is not assigned)
    GPIO.wait_for_edge(17, GPIO.RISING)
    # TODO #3 Find a proper way to let the program run infinitely

    # Clean up after stop
    GPIO.cleanup()

def isr_falling(channel):
    # TODO #1 Play sound
    print("Button " + str(get_button(channel)) + " was released")

def get_button(pin):
    # Define which button is connected to which pin
    buttons = {
        16: 0
    }
    # TODO #2 Setup other buttons/pins

    return buttons.get(pin)

if __name__ == "__main__":
    setup()
    main()
