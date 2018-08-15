import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)

pwm = GPIO.PWM(0, 100)
pwm.start(5)

def update(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    
update(100)
