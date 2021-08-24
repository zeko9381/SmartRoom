from gpiozero import Button, PWMLED, Device
from gpiozero.pins.pigpio import PiGPIOFactory
import pigpio
from time import sleep

pi = pigpio.pi()

# Configuration
max_brightness = 0.6
light_switch_pin = 14
pwm_frequency = 30000 # Must be this high, otherwise the interference is audible on the speaker
light_pin = 18

light_switch = Button(light_switch_pin, bounce_time=0.01)

def light_on(fade = True):
    if fade:
        for i in range(0, int(1000000 * max_brightness), int(1000 * max_brightness)):
            pi.hardware_PWM(light_pin, pwm_frequency, i)
    else:
        pi.hardware_PWM(light_pin, pwm_frequency, max_brightness)
        
def light_off(fade = True):
    if fade:
        for i in range(int(1000000 * max_brightness), 0, int(-1000 * max_brightness)):
            pi.hardware_PWM(light_pin, pwm_frequency, i)
    else:
        pi.hardware_PWM(light_pin, pwm_frequency, max_brightness)
        
# If you want to pass arguments, use lambda (Example: lambda: light_on(fade_time = 3))
light_switch.when_pressed = light_on
light_switch.when_released = light_off

while True:
    sleep(10)
