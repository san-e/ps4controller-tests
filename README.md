# ps4controller-tests

This Python script, "ps4controller-tests," interfaces with a PlayStation 4 controller using the pyPS4Controller library. It enables users to gather input from a PS4 controller and perform actions based on various button presses and joystick movements.
Requirements

    pyPS4Controller

# Installation

Clone this repository to your local machine:


    git clone https://github.com/san-e/ps4controller-tests.git

Install the required dependencies using pip:

    pip install pyPS4Controller

# Usage

Ensure your PlayStation 4 controller is connected to your system. Check the name of the input device using `ls /dev/input | grep "js"`. Adjust the interface in the script to reference your controller.

Navigate to the directory where the script is located.

Run the script:

    python ps4controller_tests.py

# Notes

This script assumes the PS4 controller is connected via the default interface "/dev/input/js0".
