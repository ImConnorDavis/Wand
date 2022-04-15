import RPi.GPIO as GPIO
import time

channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def callback(channel):
    if GPIO.input(channel):
        print "movement detected"
    else:
        print "movement not detected"
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=200)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
