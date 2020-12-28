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

# classmethod speaker.play_file(file_name)
# 사운드 파일을 재생합니다.
# Parameters
# • file_name(str) – 사운드 파일의 경로(확장 요소 포함).
#   you can choose one of below.
# • volume(percentage: %) – 사운드 음량 (Default: 100).
    # SoundFile.BLACK
    # SoundFile.BLUE
    # SoundFile.BROWN
    # SoundFile.DOWN
    # SoundFile.GREEN
    # SoundFile.LEFT
    # SoundFile.RED
    # SoundFile.RIGHT
    # SoundFile.UP
    # SoundFile.WHITE
    # SoundFile.YELLOW
    # SoundFile.EV3
    # SoundFile._BASE_PATH
    # SoundFile.CAT_PURR
    # SoundFile.DOG_BARK_1
    # SoundFile.DOG_BARK_2
    # SoundFile.DOG_GROWL
    # SoundFile.DOG_SNIFF
    # SoundFile.DOG_WHINE
    # SoundFile.ELEPHANT_CALL
    # SoundFile.INSECT_BUZZ_1
    # SoundFile.INSECT_BUZZ_2
    # SoundFile.INSECT_CHIRP
    # SoundFile.SNAKE_HISS
    # SoundFile.SNAKE_RATTLE
    # SoundFile.T_REX_ROAR
    # SoundFile.BRAVO
    # SoundFile.FANTASTIC
    # SoundFile.GAME_OVER
    # SoundFile.GO
    # SoundFile.GOOD
    # SoundFile.GOOD_JOB
    # SoundFile.GOODBYE
    # SoundFile.HELLO
    # SoundFile.HI
    # SoundFile.LEGO
    # SoundFile.MINDSTORMS
    # SoundFile.MORNING
    # SoundFile.NO
    # SoundFile.OKAY
    # SoundFile.OKEY_DOKEY
    # SoundFile.SORRY
    # SoundFile.THANK_YOU
    # SoundFile.YES
    # SoundFile.BOING
    # SoundFile.BOO
    # SoundFile.CHEERING
    # SoundFile.CRUNCHING
    # SoundFile.CRYING
    # SoundFile.FANFARE
    # SoundFile.KUNG_FU
    # SoundFile.LAUGHING_1
    # SoundFile.LAUGHING_2
    # SoundFile.MAGIC_WAND
    # SoundFile.OUCH
    # SoundFile.SHOUTING
    # SoundFile.SMACK
    # SoundFile.SNEEZING
    # SoundFile.SNORING
    # SoundFile.UH_OH
    # SoundFile.ACTIVATE
    # SoundFile.ANALYZE
    # SoundFile.BACKWARDS
    # SoundFile.COLOR
    # SoundFile.DETECTED
    # SoundFile.ERROR
    # SoundFile.ERROR_ALARM
    # SoundFile.FLASHING
    # SoundFile.FORWARD
    # SoundFile.OBJECT
    # SoundFile.SEARCHING
    # SoundFile.START
    # SoundFile.STOP
    # SoundFile.TOUCH
    # SoundFile.TURN
    # SoundFile.AIR_RELEASE
    # SoundFile.AIRBRAKE
    # SoundFile.BACKING_ALERT
    # SoundFile.HORN_1
    # SoundFile.HORN_2
    # SoundFile.LASER
    # SoundFile.MOTOR_IDLE
    # SoundFile.MOTOR_START
    # SoundFile.MOTOR_STOP
    # SoundFile.RATCHET
    # SoundFile.SONAR
    # SoundFile.TICK_TACK
    # SoundFile.SPEED_DOWN
    # SoundFile.SPEED_IDLE
    # SoundFile.SPEED_UP
    # SoundFile.ZERO
    # SoundFile.ONE
    # SoundFile.TWO
    # SoundFile.THREE
    # SoundFile.FOUR
    # SoundFile.FIVE
    # SoundFile.SIX
    # SoundFile.SEVEN
    # SoundFile.EIGHT
    # SoundFile.NINE
    # SoundFile.TEN
    # SoundFile.CLICK
    # SoundFile.CONFIRM
    # SoundFile.GENERAL_ALERT
    # SoundFile.OVERPOWER
    # SoundFile.READY

# Play preloaded file
ev3.speaker.set_volume(25)
ev3.speaker.play_file(SoundFile.READY)

# Play user custom file
# ev3.speaker.set_volume(25)
ev3.speaker.play_file("Half_of_Time.wav") # [a-z_].wav
