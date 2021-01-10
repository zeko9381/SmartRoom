#app.py

from flask import Flask, request #import main Flask class and request object
#Imports for DHT22
from pyA20.gpio import gpio
from pyA20.gpio import port
#import RPi.GPIO as GPIO
import dht
#from . import dht
import time
import datetime
import subprocess

app = Flask(__name__) #create the Flask app
bashCommand = "mpg123 /home/smartroom/audio/music.mp3"

# initialize GPIO
PIN2 = port.PA6
gpio.init()

# read data using pin
instance = dht.DHT(pin=PIN2)

@app.route('/', methods=['GET'])
def query_example():
    while True:
        result = instance.read()
        if result.is_valid():
            return "<p>Last valid input: " + str(datetime.datetime.now()) + "</p><p>Temperature: {0:0.1f} C".format(result.temperature) + "</p><p>Humidity: {0:0.1f} %%".format(result.humidity) + "</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #run app in debug mode on port 5000
