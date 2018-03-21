#!/usr/bin/env python3
import logging
import serial
import requests
import json


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

url = 'http://localhost:5000/update'

ser = serial.Serial('/dev/ttyACM0', 115200)
logger.info('Connected to {}'.format(ser.name))

while True:
    line = ser.readline()
    logging.debug('RAW data: {}'.format(line))
    data = json.loads(line.decode('utf-8'))
    logging.debug('Data: {}'.format(line))
    try:
        r = requests.post(url, json = data, timeout=1)
    except Exception as err:
        logging.debug('Failed to post status.')

    if r:
        logging.debug('Received response ({}): {}'.format(r.status_code, r.text))
