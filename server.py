#!/bin/python3

from flask import Flask, jsonify, abort, request
import json
import RPi.GPIO as GPIO
import pygame
from os import listdir
from os.path import isfile, join

buttons = {
    18: "0",
    23: "1",
    4: "2",
    17: "3",
    27: "4",
    22: "5",
    24: "6",
    25: "7",
    12: "8",
    16: "9",
    5: "10",
    6: "11",
    13: "12",
    19: "13",
    26: "14",
}

app = Flask(__name__)

sound_files = {
    "0": "dumm.wav",
    "1": "dumm.wav",
    "2": "dumm.wav",
    "3": "dumm.wav",
    "4": "dumm.wav",
    "5": "dumm.wav",
    "6": "dumm.wav",
    "7": "dumm.wav",
    "8": "dumm.wav",
    "9": "dumm.wav",
    "10": "dumm.wav",
    "11": "dumm.wav",
    "12": "dumm.wav",
    "13": "dumm.wav",
    "14": "dumm.wav",
}


def setup():
    global buttons
    global sound_files
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

    get_sound_files_from_mappings_json()

    print("Setup completed!")


def get_sound_files_from_mappings_json():
    global sound_files

    # TODO #4: Check if file exists
    with open('mapping.json') as fp:
        sound_files = json.load(fp)


def write_sound_file_mappings_json():
    global sound_files

    with open('mapping.json', 'w') as fp:
        json.dump(sound_files, fp)


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
    return './sound/' + str(sound_files.get(button))


def play(pin):
    button = get_button(pin)
    sound_file = get_sound_file(button)

    print("Loading sound file " + str(sound_file))

    pygame.mixer.music.load(sound_file)
    print("Playing sound file " + str(sound_file))
    pygame.mixer.music.play(0)


@app.route('/sounds', methods=["GET"])
def get_sounds():
    existing_sound_files = [f for f in listdir('./sound') if isfile(join('./sound', f))]

    return jsonify(existing_sound_files)


@app.route('/buttons', methods=["GET"])
def get_buttons():
    global sound_files

    return jsonify(sound_files)


@app.route('/buttons', methods=["POST"])
def set_buttons():
    global sound_files

    if not request.is_json:
        abort(400)
    sound_files = request.get_json()

    write_sound_file_mappings_json()

    return jsonify(sound_files)


def main():
    global app

    setup()

    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
