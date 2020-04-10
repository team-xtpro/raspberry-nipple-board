#!/bin/python3

from time import sleep
import RPi.GPIO as GPIO
import pygame

buttons = {
        18: 0,
        23: 1,
        4: 2,
        17: 3,
        27: 4,
        22: 5,
        24: 6,
        25: 7,
        12: 8,
        16: 9,
        5: 10,
        6: 11,
        13: 12,
        19: 13,
        26: 14,
    }

sound_files = {
    0: "sound/dumm.wav",
    1: "sound/dumm.wav",
    2: "sound/dumm.wav",
    3: "sound/dumm.wav",
    4: "sound/dumm.wav",
    5: "sound/dumm.wav",
    6: "sound/dumm.wav",
    7: "sound/dumm.wav",
    8: "sound/dumm.wav",
    9: "sound/dumm.wav",
    10: "sound/dumm.wav",
    11: "sound/dumm.wav",
    12: "sound/dumm.wav",
    13: "sound/dumm.wav",
}

def setup():
    global buttons
    print("Setup...")

    # Use BCM mode
    GPIO.setmode(GPIO.BCM)

    # Setup input pins
    for gpio_pin in buttons.keys():
        # Configure pins as input
        GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # Register event listeners for GPIOs
        GPIO.add_event_detect(gpio_pin, GPIO.FALLING, callback=isr_falling, bouncetime=150)

    # Initialize pygame
    pygame.mixer.init()

    print("Setup completed!")

def main():
    print("Run...")

    # Wait endlessly (18 is not assigned)
    sleep(5000)
    # TODO #3 Find a proper way to let the program run infinitely

    # Clean up after stop
    GPIO.cleanup()

def isr_falling(pin):
    print("Button " + str(get_button(pin)) + " was released")
    play(pin)

def get_button(pin):
    global buttons

    # Define which button is connected to which pin
    return buttons.get(pin)

def get_sound_file(button):
    global sound_files

    # Define which sound file to play according to the pressed button
    return sound_files.get(button)

def play(pin):
    button = get_button(pin)
    sound_file = get_sound_file(button)

    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(0)

if __name__ == "__main__":
    setup()
    main()
