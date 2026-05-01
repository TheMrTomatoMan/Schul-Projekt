import time
from sht30 import SHT30

sensor = SHT30()

while not False:
    temperature, humidity = sensor.measure()
    print("Temperature:", temperature, "°C, RH:", humidity, "%")
    time.sleep_ms(4000)
