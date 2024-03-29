# HEX - Biomimetic Robotics

This project features the fusion of biomimetic principles with robotics and artificial intelligence, culminating in a hexapod robot equipped with a simple reflex agent AI. The robot, featuring a 3D-printed exoskeleton and powered by a Raspberry Pi, uses two 16 channel Adafruit I2C board and soldered components to facilitate efficient operation. An ultrasound proximity sensor integrated into the system allows for effective interaction with the robot's environment. The entire system was programmed using Python, highlighting its application in practical, interactive, and autonomous robotics.

Video playlist:
https://www.youtube.com/playlist?list=PLzvBwCPNuxcbhuNtr4e46624VTsDVG8bE

![Alt text](hex/assets/hex-robot.jpg)

## Execution

```bash
# Initialise instance:
from hexy.robot.hexapod import Hexapod
hex = Hexapod()

# Basic Low level Python Commands:
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
```

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.