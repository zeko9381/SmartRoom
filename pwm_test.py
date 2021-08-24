import pigpio
from time import sleep

pwm_pin = 18
pwm_frequency = 30000
max_brightness = 0.6

pi = pigpio.pi()

for i in range(0, int(1000000 * max_brightness), 1000):
    pi.hardware_PWM(pwm_pin, pwm_frequency, i)
    print(i)
    #sleep(0.01)
#pi.hardware_PWM(pwm_pin, pwm_frequency, 0)
