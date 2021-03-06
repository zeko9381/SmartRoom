from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

gpio.init() #Initialize module. Always called first

#Konfiguracija
switch_port = port.PA10

gpio.setcfg(switch_port, gpio.INPUT)
#gpio.pullup(switch_port, 0)

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

state = gpio.input(switch_port)
last_state = state

try:
    while True:
        state = gpio.input(switch_port)

        if state != last_state:
            if state == 1:
                for i in reversed(range(0, 200000, 100)):
                    duty_cycle = open("/sys/class/pwm/pwmchip0/pwm0/duty_cycle", "w")
                    duty_cycle.write(str(i))
                    duty_cycle.close()

            elif state == 0:
                for i in range(0, 200000, 100):
                    duty_cycle = open("/sys/class/pwm/pwmchip0/pwm0/duty_cycle", "w")
                    duty_cycle.write(str(i))
                    duty_cycle.close()

        last_state = state
        sleep(0.001) # Without this, the CPU gets pinned to 100%

except KeyboardInterrupt:
    print("Exiting...")

    enable = open("/sys/class/pwm/pwmchip0/pwm0/enable", "w")
    enable.write("0")
    enable.close()

    unexport = open("/sys/class/pwm/pwmchip0/unexport", "w")
    unexport.write("0")
    unexport.close()

    print("Exited!")
