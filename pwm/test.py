from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

gpio.init()

# Set GPIO pin PA6 as PWM output with a frequency of 100 Hz
pwm = OrangePwm(500, port.PA12)

# Start PWM output with a duty cycle of 20%. The pulse (HIGH state) will have a duration of
# (1 / 100) * (20 / 100) = 0.002 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 20) / 100) = 0.008 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 20% of its capacity.
#pwm.start(20)
#sleep(2)

# Change duty cycle to 6%. The pulse (HIGH state) will now have a duration of
# (1 / 100) * (6 / 100) = 0.0006 seconds, followed by a low state with a duration of
# (1 / 100) * ((100 - 6) / 100) = 0.0094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity.
#pwm.changeDutyCycle(6)
#sleep(2)

# Change the frequency of the PWM pattern. The pulse (HIGH state) will now have a duration of
# (1 / 10) * (6 / 100) = 0.006 seconds, followed by a low state with a duration of
# (1 / 10) * ((100 - 6) / 100) = 0.094 seconds.
# If a LED is plugged to with GPIO pin, it will shine at 6% of its capacity, but you may
# notice flickering.
#pwm.changeFrequency(10)
#sleep(2)

# Stop PWM output
#pwm.stop()
i = 0

pwm.start(0)

while True:
	pwm.changeDutyCycle(i)
	i = i + 1
	sleep(0.1)
	
	if i == 100:
		i = 0
