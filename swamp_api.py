import os
import subprocess
import json

from flask import Flask
from flask import jsonify

app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))

@app.route('/swamp/on', methods=['GET'])
def swamp_on():
    subprocess.check_output("irsend SEND_ONCE swamp KEY_4", shell=True)
    data = {'message':'ok'}
    return jsonify(data), 200

@app.route('/swamp/pre-wet', methods=['GET'])
def swamp_pre_wet():
    subprocess.check_output("irsend SEND_ONCE swamp KEY_6", shell=True)
    data = {'message':'ok'}
    return jsonify(data), 200

@app.route('/swamp/low-vent', methods=['GET'])
def swamp_low_vent():
    subprocess.check_output("irsend SEND_ONCE swamp KEY_1", shell=True)
    data = {'message':'ok'}
    return jsonify(data), 200

@app.route('/swamp/high-vent', methods=['GET'])
def swamp_high_vent():
    subprocess.check_output("irsend SEND_ONCE swamp KEY_2", shell=True)
    data = {'message':'ok'}
    return jsonify(data), 200

@app.route('/swamp/low-cool', methods=['GET'])
def swamp_low_cool():
    subprocess.check_output("irsend SEND_ONCE swamp KEY_4", shell=True)
    data = {'message':'ok'}
    return jsonify(data), 200

@app.route('/swamp/high-cool', methods=['GET'])
def swamp_high_cool():
    subprocess.check_output("irsend SEND_ONCE swamp KEY_5", shell=True)
    data = {'message':'ok'}
    return jsonify(data), 200

@app.route('/swamp/off', methods=['GET'])
def swamp_off():
    subprocess.check_output("irsend SEND_ONCE swamp KEY_6", shell=True)
    subprocess.check_output("sleep 2", shell=True)
    subprocess.check_output("irsend SEND_ONCE swamp KEY_0", shell=True)
    data = {'message':'ok'}
    return jsonify(data), 200

@app.route('/temp', methods=['GET'])
def temp():
    command = '/usr/bin/python ' + path + '/therm.py  -s'
    output = subprocess.Popen("command")
    data = {"message":output}
    return jsonify(data), 200

if __name__ == '__main__':
     app.run(port='80',host='0.0.0.0')
