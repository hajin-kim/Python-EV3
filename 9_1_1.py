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

# The following loop makes the robot drive forward until it detects an
# obstacle. Then it backs up and turns around. It keeps on doing this
# until you stop the program.
while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(200, 0)
    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing(waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while obstacleSensor.distance() > 300:
        wait(10)
    # Drive backward at 100 millimeters per second. Keep going for 2 seconds.
    robot.drive(-100, 0)
    wait(2000)
    # Turn around at 60 degrees per second, around the midpoint between
    # the wheels. Keep going for 2 seconds.
    robot.drive(0, 60)
    wait(2000)

