import json
from hygrometer import boden_feuchte
from sht30_output import sht_humidity, sht_temp
from thermometer import temperatur2
import time

def json_write():
    t = time.localtime()
    timestamp = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])

    json_str = (
        '{{\n'
        '  "Time": "{}",\n'
        '  "Temperatur von SHT30": "{}",\n'
        '  "Luftfeuchte von SHT30": "{}",\n'
        '  "Temeratur von Sensor": "{}",\n'
        '  "Boden Feuchtigkeit": "{}"\n'
        '}}'
    ).format(
        timestamp,
        "{}°C".format(sht_temp()),
        "{}%Rel".format(sht_humidity()),
        "{}°C".format(temperatur2()),
        "{}%".format(boden_feuchte())
    )

    with open("data.json", "w") as f:
        f.write(json_str)