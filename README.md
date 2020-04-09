# Raspberry Nipple Board

Nipple board running on a Raspberry Pi

## Getting started

To develop the nipple board, you will need a basic setup.

### Hardware

| Amount | Description      |
|--------|------------------|
| 1      | Raspberry Pi     |
| 1      | Breadboard       |
| 1      | Button           |
| 1      | 120 Ohm resistor |
| 1      | LED red          |
| Some   | Cables           |

### Software

For development, you could use any editor of choice, but for convenience, I use PyCharm with a remote debugger running
on the RPi via SSH.

[Set up remote debuggin on RPi with PyCharm](https://www.jetbrains.com/help/pycharm/remote-development-on-raspberry-pi.html)

## Configuration

In this project we're using BCM as pin configuration.

### Pin configuration

| Pin | Configuration      |
|-----|--------------------|
| 16  | Input              |
| 17  | Input (but unused) |
| 21  | Output             |
