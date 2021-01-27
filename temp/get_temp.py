from flask import Flask, request #import main Flask class and request object
#Imports for DHT22
from pyA20.gpio import gpio
from pyA20.gpio import port
#import RPi.GPIO as GPIO
import dht
import time
import datetime
import subprocess
import threading
from queue import Queue

app = Flask(__name__) #create the Flask app
#bashCommand = "mpg123 /home/smartroom/audio/music.mp3"

# initialize GPIO
PIN2 = port.PA6
gpio.init()

# read data using pin
instance = dht.DHT(pin=PIN2)

qtemp = Queue()
qhum = Queue()

def getTemp(qtemp_out, qhum_out):
    while True:
        result = instance.read()
        if result.is_valid():
            print(str(datetime.datetime.now()) + ": Result is valid!")
            temp = result.temperature
            qtemp_out.put(temp)
            hum = result.humidity
            qhum_out.put(hum)
        time.sleep(1)
            
getTempThread = threading.Thread(target = getTemp, args = (qtemp, qhum))
getTempThread.start()
print("* getTempThread running...")

@app.route('/api', methods=['POST'])
def query():
    #lightBrightness = request.form.get('light')
    print("* Request data: " + str(request.form.get('event')))
    
    if request.form.get('brightness'):
        brightness = request.form.get('brightness')
        print("* Setting brightness...")
    elif request.form.get('event'):
        event = request.form.get('event')
        print("* Starting event " + event)
    elif not request.data:
        return '{"temperature":' + str(qtemp.get()) + ',"humidity":' + str(qhum.get()) + '}'

    return "{}"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #run app in debug mode on port 5000
