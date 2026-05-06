import json
from hygrometer import boden_feuchte
from sht30_output import sht_humidity, sht_temp 
from thermometer import temperatur2
from datetime import datetime

data = {"Time": f"{datetime.now().strftime("%H:%M:%S")}",
        "Boden Feuchtigkeit": f"{boden_feuchte()}%",
        "Temperatur von SHT30": f"{sht_temp()}°C",
        "Luftfeuchte von SHT30": f"{sht_humidity()}%Rel",
        "Temeratur von Sensor": f"{temperatur2()}°C"
        }
json_str = json.dumps(data)
json_str = json_str.replace(",", ",\n")
def json_write():
    with open ("data.json", "w") as f:
        f.write(json_str)