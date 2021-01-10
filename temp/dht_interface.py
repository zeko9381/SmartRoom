'''
@author: zorbac

Copyright 2014 zorbac at free.fr
This code is free software; you can redistribute it and/or modify it
under the terms of the BSD license (see the file
COPYING.txt included with the distribution).
'''

from . import dht
from pyA20.gpio import gpio
from pyA20.gpio import port
import datetime


class DHTInterface(object):
    '''
    classdocs
    '''

    def __init__(self, pa_number=0, sensor=22, debug=False):
        '''
        Constructor
        '''
        # initialize GPIO
        if 0 == pa_number:
            self._pin = port.PA0
        elif 1 == pa_number:
            self._pin = port.PA1

        self._sensor = sensor
        
        self._debug = debug
        gpio.init()

        # read data using pin 
        self._instance = dht.DHT(pin=self._pin, sensor=sensor)

    def get_valeurs(self):
        counter = 0
        result = self._instance.read()
        while not result.is_valid() and counter < 20:
            result = self._instance.read()
            counter += 1

        if self._debug:
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: {0:0.1f} C".format(result.temperature))
            print("Humidity: {0:0.1f} %%".format(result.humidity))

        return result.temperature, result.humidity
    
    def get_sensor(self):
        return self._sensor
