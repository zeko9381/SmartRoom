from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
from orangepwm import *

gpio.init() #Initialize module. Always called first

gpio.setcfg(port.PA12, gpio.OUTPUT)  #Configure LED1 as output
gpio.output(port.PA12, gpio.HIGH)
