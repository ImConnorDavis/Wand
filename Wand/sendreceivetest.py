import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
print("LED on")


channel = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(2,GPIO.HIGH)

def callback(channel):
    if GPIO.input(channel):
        print "movement detected"
        GPIO.output(2,GPIO.LOW)
    else:
        print "movement not detected"
        GPIO.output(2,GPIO.LOW)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=200)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
