from pyA20.gpio import gpio
from pyA20.gpio import port

#import RPi.GPIO as GPIO
import dht
#from . import dht
import time
import datetime

# initialize GPIO
PIN2 = port.PA6
gpio.init()

# read data using pin
instance = dht.DHT(pin=PIN2)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: {0:0.1f} C".format(result.temperature))
        print("Humidity: {0:0.1f} %%".format(result.humidity))

    time.sleep(1)
