#!/usr/bin/env python3

def moveZone( cl, mB, mC, count ):
    x = 0
    while (x < count):
        #Role one centimer
        mB.run_timed(time_sp=500, speed_sp=500)
        mC.run_timed(time_sp=500, speed_sp=500)
        mB.wait_while('running')

        while True:    # exit loop when any button pressed
            if cl.value()>30:   # weak reflection so over black line
                # medium turn right
                mB.run_forever(speed_sp=450)
                mC.run_forever(speed_sp=455)
            else:
                mB.stop(stop_action='brake')
                mC.stop(stop_action='brake')
                break
        x = x + 1

def moveBackZone( cl, mB, mC, count ):
    x = 0
    while (x < count):
        #Role one centimer
        mB.run_timed(time_sp=500, speed_sp=-500)
        mC.run_timed(time_sp=500, speed_sp=-500)
        mB.wait_while('running')

        while True:    # exit loop when any button pressed
            if cl.value()>30:   # weak reflection so over black line
                # medium turn right
                mB.run_forever(speed_sp=-450)
                mC.run_forever(speed_sp=-450)
            else:
                mB.stop(stop_action='brake')
                mC.stop(stop_action='brake')
                break
        x = x + 1

def grabItem ( mA ):
    mA.run_timed(time_sp=1000, speed_sp=500)
    mA.wait_while('running')

def dropItem ( mA ):
    mA.run_timed(time_sp=1000, speed_sp=-500)
    mA.wait_while('running')

def turnAround ( mB, mC ):
    mB.run_timed(time_sp=3500, speed_sp=500)
    mC.run_timed(time_sp=3500, speed_sp=-500)
    mB.wait_while('running')
