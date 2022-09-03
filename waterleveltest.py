import RPi.GPIO as GPIO
import time
from datetime import datetime
import csv


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)


while True:
    now = datetime.now()
    datetime_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if GPIO.input(24):
        print("No water detected " + datetime_string)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
    else:
        print("Water detected " + datetime_string)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
    time.sleep(3600)