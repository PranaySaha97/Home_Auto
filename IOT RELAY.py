import RPi.GPIO as GPIO
import time 
from ubidots import ApiClient

led = 3

api = ApiClient(token= 'A1E-WLuKlvx6mrCQVf22RF45pLuVlE0yrY')
var = api.get_variable("5c5dee81c03f971822e82a47")

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 0)

while True:
    last_value = var.get_values(1)
    print (last_value[0]['value'])
    if last_value[0]['value']:
        GPIO.output(led, 1)
        time.sleep(1)
    else:
        GPIO.output(led, 0)
        time.sleep(1)
