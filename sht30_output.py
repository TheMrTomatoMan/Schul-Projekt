import time
from sht30.py import SHT30

sensor = SHT30()

def sht_temp():
    temperature = sensor.measure()
    return temperature

def sht_humidity():
    humidity = sensor.measure()
    return humidity
    