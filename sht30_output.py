import time
from sht30 import SHT30

sensor = SHT30()

def sht_temp():
    temperature,humidity = sensor.measure()
    temperature = round(temperature,1)
    return temperature

def sht_humidity():
    temperature,humidity = sensor.measure()
    humidity = round(humidity, 1)
    return humidity