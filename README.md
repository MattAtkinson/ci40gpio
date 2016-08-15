# ci40gpio

A Python3 example showing an LED flashing on a breadboard using the Raspberry Pi connector GPIO. This makes use of pyletmecreate (https://github.com/francois-berder/PyLetMeCreate).

By default it uses MFIO_83 (PIN 37 - See linked pinmap below), but can be configured by changing the GPIO_NUM variable.

https://docs.creatordev.io/ci40/guides/hardware/#primary-expansion-header-pinmap

## Usage

1. Connect an LED on a breadboard as normal with MFIO_83 (or your choson GPIO) connected to the longer pin and the shorter pin connected to ground via a resistor.
2. Install Python3 (opkg install python3-base python3)
3. Put the gpio_toggle.py script from this repo on the board
4. 'python3 gpio_toggle.py'

