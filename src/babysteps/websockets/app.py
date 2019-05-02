#!/usr/bin/env python3

from flask import Flask, render_template
from flask_socketio import SocketIO
import RPi.GPIO as gpio
import time, threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode='threading')

red      = 11 
green    = 9
blue     = 8

s1	 = 22
s2	 = 10

gpio.setmode(gpio.BCM)
gpio.setup(red  ,gpio.OUT)
gpio.setup(green,gpio.OUT)
gpio.setup(blue, gpio.OUT)

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

@socketio.on('connect')
def connect():
    socketio.emit('tex',{'data':{'s1':gpio.input(s1)}}) 
    socketio.emit('tex',{'data':{'s2':gpio.input(s2)}}) 

def rpiloop():
    s1last = 0
    s2last = 0
    while True:
        time.sleep(0.5)
        socketio.emit('tex',{'data':{'time':time.strftime("%y%m%d-%H%M%S",time.localtime(time.time())),'s1':gpio.input(s1),'s2':gpio.input(s2)}}) 

def flaskloop():
    socketio.run(app,host='0.0.0.0')

if __name__ == '__main__':
    threading.Thread(target=flaskloop).start()
    threading.Thread(target=rpiloop).start()


