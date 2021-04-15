from pyA20.gpio import gpio
from pyA20.gpio import port

gpio.init() #Initialize module. Always called first

button = port.PA14

gpio.setcfg(button, gpio.INPUT)
gpio.pullup(button, gpio.PULLUP)

while True:
    state = gpio.input(button)
    
    if (state == 1):
        print ("LOW")
    else:
        print ("HIGH")
