import RPi.GPIO as GPIO


def setup_fun(fan_id, speed):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(fan_id, GPIO.OUT)
    pi_pwm = GPIO.PWM(fan_id, speed)
    pi_pwm.start(0)
    return pi_pwm
