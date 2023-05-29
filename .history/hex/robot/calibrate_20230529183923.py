from core import HexapodCore
from time import sleep

def calibrate_joint(joint, t, mn, mx, z):

    while True:
        for angle in [mn, z, mx, z]:
            joint.pose(angle)
            sleep(t)
            
hex = HexapodCore()
calibrate_joint( hex.right_back.knee, t = 2, mn = -45, mx = 45, z = 0)
#hex.off()
