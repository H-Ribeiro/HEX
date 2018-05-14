# HEX

Install library:
sudo python setup.py install

Initialise instance:
from hexy.robot.hexapod import Hexapod
hex = Hexapod()


Basic Low level Python Commands:
hex.off()
hex.boot_up()
hex.auto_pod()
hex.shutdown()

hex.lie_down()
hex.curl_up()
hex.lie_flat()
hex.squat(35)


hex.curl_up()
hex.lie_down()

hex.walk(swing = 20, repetitions = 10)

hex.get_up(maxx = 30, step = 4)
