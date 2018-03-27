from ..robot.hexapod import Hexapod
from time import sleep

hex =  Hexapod()

hex.boot_up()

print "rotate left"
hex.rotate(offset = 40)

print "rotate right"
hex.rotate(offset = -40)

print "walk forward"
hex.walk()

print "walk backward"
hex.walk(swing = -10)

hex.shut_down()
