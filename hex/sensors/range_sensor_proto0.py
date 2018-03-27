import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

"""GPIO 23 [Pin 16] as TRIG, input pin (which reads the return signal from
the sensor) GPIO 24 [Pin 18] as ECHO."""
TRIG = 23
ECHO = 24

print "Distance Measurement In Progress"

"""Set two GPIO ports as either inputs or outputs as defined previously."""
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

"""Trigger pin is set low, and give the sensor a second to settle."""
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

"""The HC-SR04 sensor requires a short 10uS pulse to trigger the module, which
will cause the sensor to start the ranging program (8 ultrasound bursts at 40 kHz)
 in order to obtain an echo response. So, to create our trigger pulse, we set out
  trigger pin high for 10uS then set it low again."""
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

"""Calculate the difference between the two recorded timestamps"""
pulse_duration = pulse_end - pulse_start

"""Speed of sound at sea level is 343m/s, divided by 2 to calculate the time it
takes for the ultrasonic pulse to travel the distance to the object and back again"""
distance = pulse_duration * 17150

"""distance to 2 decimal places"""
distance = round(distance, 2)

print "Distance:",distance,"cm"

GPIO.cleanup()
