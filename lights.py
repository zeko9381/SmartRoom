from gpiozero import Button, PWMLED, Device
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

lightSwitch = Button(14, bounce_time=0.01)
light = PWMLED(18, initial_value = 0, frequency = 5000)

def light_on(fade, fade_time = 1):
    if fade:
        for i in range(0, 255, 1):
            light.value = i / 255
            sleep(fade_time / 255)
            print(light.value)
        print("ON")
    else:
        light.value = 1
    
def light_off(fade, fade_time = 1):
    if fade:
        for i in range(255, 0, -1):
            light.value = i / 255
            sleep(fade_time / 255)
            print(light.value)
    else:
        light.value = 0
        
# The lambdas are for passing arguments
lightSwitch.when_pressed = lambda: light_on(False)
lightSwitch.when_released = lambda: light_off(False)

while True:
    sleep(10)
