#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
obstacleSensor = UltrasonicSensor(Port.S3)

wheel_diameter = 56
axle_track = 114
robot = DriveBase(
    leftMotor,
    rightMotor,
    wheel_diameter,
    axle_track
    )

# Write your program here.
ev3.speaker.beep()

robot.drive(100, 0)
while True:
    wait(10)
    if obstacleSensor.distance() > 300:
        robot.drive(100, 0)
    else:
        robot.stop()

# ev3.speaker.set_volume(25) # in percentage
# ev3.speaker.play_file("Half_of_Time.wav") # [a-zA-Z_].wav

# ev3.screen.clear()
# ev3.screen.load_image("Code_in_You.png") # [a-zA-Z_].png

