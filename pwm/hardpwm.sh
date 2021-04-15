#!/bin/bash

#Export PWM channel for user control.
sh -c "echo 0 > /sys/class/pwm/pwmchip0/export"

#Select the period of PWM signal. Value is in picoseconds.
sh -c "echo 500000 > /sys/class/pwm/pwmchip0/pwm0/period"

#Change the polarity of the PWM signal.
#The polarity can only be changed if the PWM is not enabled.
sh -c "echo "normal" > /sys/class/pwm/pwmchip0/pwm0/polarity"

#Enable the PWM signal.
sh -c "echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable"

for i in {0..500000..10000}
do
	sh -c "echo $i > /sys/class/pwm/pwmchip0/pwm0/duty_cycle"
	cat /sys/class/pwm/pwmchip0/pwm0/duty_cycle
	#sleep 0.00001
done

#Disable the PWM signal.
sh -c "echo 0 > /sys/class/pwm/pwmchip0/pwm0/enable"

#UnExport PWM channel for user control.
sh -c "echo 0 > /sys/class/pwm/pwmchip0/unexport"
