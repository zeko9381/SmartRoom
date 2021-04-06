OrangePWM - Python software PWM for Orange Pi
=======

OrangePWM Python, for Orange Pi Lite, Orange Pi PC, Orange Pi Zero is easy programmatic PWM ligrary, is an easy way to implement software PWM (Pulse Width Modulation) output on Orange Pi using Python language.

* [Authors's website - RU/UA](http://evergreens.com.ua/ru/products/development/iot-devices.html)
* [Authors's website - EN](http://evergreen.team/en/products/development/iot-devices.html)
* [PiZyPwm](https://github.com/aboudou/pizypwm/tree/master/rpi.gpio)


Warning
-------

Due to the non real-time capacities of Python language, do not expect PWM to be very accurate. Pulses will never exactly last the theorical duration. But OrangePWM will be enough if you don't need a great accuracy.

Requirements
------------

* First of all : Orange Pi
* Python (with Debian / Raspbian : packages “python” and “python-dev”)
* PyA20.gpio library

Example usage
-------------

```
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

gpio.init()

# Set GPIO pin PA6 as PWM output with a frequency of 100 Hz
pwm = OrangePwm(100, port.PA6)

# Start PWM output with a duty cycle of 20%. The pulse (HIGH state) will have a duration of
# (1 / 100) * (20 / 100) = 0.002 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 20) / 100) = 0.008 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 20% of its capacity.
pwm.start(20)
sleep(2)

# Change duty cycle to 6%. The pulse (HIGH state) will now have a duration of
# (1 / 100) * (6 / 100) = 0.0006 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 6) / 100) = 0.0094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity.
pwm.changeDutyCycle(6)
sleep(2)

# Change the frequency of the PWM pattern. The pulse (HIGH state) will now have a duration of
# (1 / 10) * (6 / 100) = 0.006 seconds, followed by a low state with a duration of
# (1 / 10) * ((100 - 6) / 100) = 0.094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity, but you may
# notice flickering.
pwm.changeFrequency(10)
sleep(2)

# Stop PWM output
pwm.stop()
