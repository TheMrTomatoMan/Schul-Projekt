# Importiert alles aus sht30 als SHT30
from sht30 import SHT30
# nimmt die Daten von SHT30() und speichert sie in der variable Sensor
sensor = SHT30()

# Eine Funktion die die Temperatur Returnt und auf eine nachkommastelle rundet
def sht_temp():
    temperature,humidity = sensor.measure()
    temperature = round(temperature,1)
    return temperature

# Eine Funktion die die Luftfeuchtigkeit Returnt und auf eine nachkommastelle rundet
def sht_humidity():
    temperature,humidity = sensor.measure()
    humidity = round(humidity, 1)
    return humidity