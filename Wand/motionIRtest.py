import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)


detector = 18
motionPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(detector, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(motionPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def detection(detector):
    if GPIO.input(detector):
        print "Light Detected"
def motion(motionPin):
    if GPIO.input(motionPin):
        print("Movement Detected")
        GPIO.output(2,GPIO.HIGH)
GPIO.add_event_detect(detector, GPIO.BOTH, bouncetime=200)
GPIO.add_event_callback(detector, detection)
GPIO.add_event_detect(motionPin, GPIO.BOTH, bouncetime=200)
GPIO.add_event_callback(motionPin, motion)

while True:
    time.sleep(1)
