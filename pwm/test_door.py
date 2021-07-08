from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

gpio.init() #Initialize module. Always called first

button = port.PA12

gpio.setcfg(button, gpio.INPUT)
#gpio.pullup(button, 0)

#PWM setup
export = open("/sys/class/pwm/pwmchip0/export", "w")
export.write("0")
export.close()

period = open("/sys/class/pwm/pwmchip0/pwm0/period", "w")
period.write("500000")
period.close()

polarity = open("/sys/class/pwm/pwmchip0/pwm0/polarity", "w")
polarity.write("normal")
polarity.close()

enable = open("/sys/class/pwm/pwmchip0/pwm0/enable", "w")
enable.write("1")
enable.close()

#state = gpio.input(button)
#last_state = state

try:
    while True:
        #state = gpio.input(button)
        
        if (gpio.input(button) == gpio.LOW):
            print ("LOW")
            duty_cycle = open("/sys/class/pwm/pwmchip0/pwm0/duty_cycle", "w")
            duty_cycle.write("0")
            duty_cycle.close()
        else:
            print ("HIGH")
            duty_cycle = open("/sys/class/pwm/pwmchip0/pwm0/duty_cycle", "w")
            duty_cycle.write("150000")
            duty_cycle.close()
        
except KeyboardInterrupt:
    print("Exiting...")
    
    enable = open("/sys/class/pwm/pwmchip0/pwm0/enable", "w")
    enable.write("0")
    enable.close()

    unexport = open("/sys/class/pwm/pwmchip0/unexport", "w")
    unexport.write("0")
    unexport.close()
    
    print("Exited!")
