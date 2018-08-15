import RPi.GPIO as GPIO

def clean():
    GPIO.setwarnings(False)
    GPIO.cleanup()
