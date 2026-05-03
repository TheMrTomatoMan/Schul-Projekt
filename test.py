import time
from hygrometer import boden_feuchte
from sht30_output import sht_humidity
from sht30_output import sht_temp
from thermometer import temperatur2
from write_to_json import json_write


while True:
    print(f"Boden Feuchte: {boden_feuchte()}%")
    print(f"Temperatur on Board: {sht_temp()}°C")
    print(f"Luftfeuchtigkeit on Board: {sht_humidity()}% Rel")
    print(f"Temperatur an Temperatur sensor: {temperatur2()}°C")
    json_write()
    time.sleep(5)

