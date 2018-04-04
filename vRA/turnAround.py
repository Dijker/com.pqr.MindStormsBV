#!/usr/bin/env python3
from ev3dev.ev3 import *

# Connect EV3 color sensor.
cl = ColorSensor()

#Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
cl.mode='COL-REFLECT'

#Attach medium motor to port A
mA = MediumMotor('outA')

mB.run_timed(time_sp=3500, speed_sp=500)
mC.run_timed(time_sp=3500, speed_sp=-500)
