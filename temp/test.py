from pyA20.gpio import gpio
from pyA20.gpio import port

#import RPi.GPIO as GPIO
import dht
#from . import dht
import time
import datetime
import subprocess

# initialize GPIO
PIN2 = port.PA6
gpio.init()

# read data using pin
instance = dht.DHT(pin=PIN2)

bashCommand = "mpg123 /home/smartroom/music.mp3"

while True:
    result = instance.read()

    if result.is_valid():
        temp = result.temperature
        print(temp)
        if (temp >= 26):
            print("Play music!!!!")
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            break

    time.sleep(0.5)
        

    #if result.is_valid() && result.temperature() = 26:
        #print("Last valid input: " + str(datetime.datetime.now()))
        #print("Temperature: {0:0.1f} C".format(result.temperature))
        #print("Humidity: {0:0.1f} %%".format(result.humidity))

#    time.sleep(1)
#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
