#!/usr/bin/env python3
from ev3dev.ev3 import *
from functions import *

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

btn = Button() # will use any button to stop script

moveZone(cl,mB,mC,1)

grabItem(mA)

moveZone(cl,mB,mC,1)

dropItem(mA)

moveBackZone(cl,mB,mC,2)

print("End program!")
