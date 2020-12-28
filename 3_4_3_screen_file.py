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


# Write your program here.
ev3.speaker.beep()

# classmethod screen.load_image(file_name)
# 이미지 파일을 표시합니다.
# Parameters
# • file_name(str) – 이미지 파일의 경로. 경로는 절대 경로이거나 프로젝트 폴더에 대비한 상대 경로일 수 있습니다.
    # ImageFile.DOWN
    # ImageFile.LEFT
    # ImageFile.RIGHT
    # ImageFile.UP
    # ImageFile.EV3
    # ImageFile.BOTTOM_LEFT
    # ImageFile.BOTTOM_RIGHT
    # ImageFile._BASE_PATH
    # ImageFile.FORWARD
    # ImageFile.ANGRY
    # ImageFile.AWAKE
    # ImageFile.BLACK_EYE
    # ImageFile.CRAZY_1
    # ImageFile.CRAZY_2
    # ImageFile.DISAPPOINTED
    # ImageFile.DIZZY
    # ImageFile.EVIL
    # ImageFile.HURT
    # ImageFile.KNOCKED_OUT
    # ImageFile.LOVE
    # ImageFile.MIDDLE_LEFT
    # ImageFile.MIDDLE_RIGHT
    # ImageFile.NEUTRAL
    # ImageFile.NUCLEAR
    # ImageFile.PINCHED_LEFT
    # ImageFile.PINCHED_MIDDLE
    # ImageFile.PINCHED_RIGHT
    # ImageFile.SLEEPING
    # ImageFile.TEAR
    # ImageFile.TIRED_LEFT
    # ImageFile.TIRED_MIDDLE
    # ImageFile.TIRED_RIGHT
    # ImageFile.TOXIC
    # ImageFile.WINKING
    # ImageFile.ACCEPT
    # ImageFile.BACKWARD
    # ImageFile.DECLINE
    # ImageFile.NO_GO
    # ImageFile.QUESTION_MARK
    # ImageFile.STOP_1
    # ImageFile.STOP_2
    # ImageFile.THUMBS_DOWN
    # ImageFile.THUMBS_UP
    # ImageFile.WARNING
    # ImageFile.EV3_ICON
    # ImageFile.TARGET

# Show a built-in image of two eyes looking upward
ev3.screen.load_image(ImageFile.UP)

