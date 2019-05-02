#!/usr/bin/env python3

from flask import Flask, render_template
from flask_socketio import SocketIO
import RPi.GPIO as gpio
import time, threading


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

red      = 11 
green    = 9
blue     = 8
s1	 = 22
s2	 = 10

s1last   = 0
s2last   = 0

gpio.setmode(gpio.BCM)
gpio.setup(red  ,gpio.OUT)
gpio.setup(green,gpio.OUT)
gpio.setup(blue, gpio.OUT)
gpio.setmode(gpio.BCM)
gpio.setup(s1,   gpio.IN)
gpio.setup(s2,   gpio.IN)


@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('tex')
def tex_event(json):
    print('received tex_event: ' + str(json))
    # print('received data: ' + json['data'])
    data = json['data']
    try:
        gpio.output(red, data['red']);
    except:
        pass
    try:
        gpio.output(green, data['green']);
    except:
        pass
    try:
        gpio.output(blue, data['blue']);
    except:
        pass

def rpiloop():
    s1last = 0
    s2last = 0
    while True:
        s1state = gpio.input(s1)
        if s1state != s1last:
            socketio.emit('tex',{'data':{'s1':s1state}}) 
            print("s1 diff")
            s1last = s1state
        s2state = gpio.input(s2)
        if s2state != s2last:
            socketio.emit('tex',{'data':{'s2':s2state}}) 
            print("s2 diff")
            s2last = s2state
        time.sleep(0.1)

def flaskloop():
    socketio.run(app,host='0.0.0.0',debug=True)


if __name__ == '__main__':
    threading.Thread(target=flaskloop).start()
    threading.Thread(target=rpiloop).start()


