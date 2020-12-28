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
# Initialize two motors with default settings on Port B and Port C.
# These will be the left and right motors of the drive base.
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
obstacleSensor = UltrasonicSensor(Port.S3)

# The wheel diameter of the Robot Educator is 56 millimeters.
wheel_diameter = 56
# The axle track is the distance between the centers of each of the wheels.
# For the Robot Educator this is 114 millimeters.
axle_track = 114
# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
robot = DriveBase(leftMotor, rightMotor, wheel_diameter, axle_track)


# Write your program here.
ev3.speaker.beep()

# Drive forward at 100 mm/s for 1 seconds
robot.drive(100, 0)
wait(1000)
robot.stop()

# Turn at 45 deg/s for 1 seconds
robot.drive(0, 45)
wait(1000)
robot.stop()

# Drive forward at 100 mm/s for 1 seconds
robot.drive(100, 0)
wait(1000)
robot.stop()
