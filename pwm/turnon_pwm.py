from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
from orangepwm import *

gpio.init() #Initialize module. Always called first

pwm = OrangePwm(2000, port.PA12)
pwm.start(15)
