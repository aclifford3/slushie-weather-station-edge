import RPi.GPIO as GPIO
import time
import dht11
from graphql.slushie_client import SlushieClient
import config

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 25
instance = dht11.dht11.DHT11(pin = 25)
result = instance.read()

def loop():
    client = SlushieClient()
    while(True):
        if result.is_valid():
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            client.update_weather_data(config.DEVICE_ID, temperature=result.temperature, humidity=result.humidity)
        else:
            print("Error: %d" % result.error_code)
        time.sleep(1)

loop()
