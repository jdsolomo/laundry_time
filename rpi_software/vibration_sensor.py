import time
import grovepi

# Connect the Grove Piezo Vibration Sensor to analog port A0
# OUT,NC,VCC,GND
piezo = 0

grovepi.pinMode(piezo,"INPUT")

while True:
    try:
        # When vibration is detected, the sensor outputs a logic high signal
        vibration_avg=0
        for i in range(10):
        	vib= grovepi.analogRead(piezo)
        	time.sleep(.1)
        	vibration_avg+=vib
        vibration_avg=vibration_avg/10

    except IOError:
        print "Error"