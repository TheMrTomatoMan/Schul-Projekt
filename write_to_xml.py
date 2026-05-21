from thermometer import temperatur2
from sht30_output import sht_temp, sht_humidity
from hygrometer import boden_feuchte
import time

def xml_write():
    t = time.localtime()
    timestamp = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])

    xml = """<?xml version="1.0" encoding="UTF-8"?>
<sensordaten>
    <Time>{time}</Time>
    <Boden_Feuchtigkeit>{boden}%</Boden_Feuchtigkeit>
    <Temperatur_SHT30>{temp_sht}C</Temperatur_SHT30>
    <Luftfeuchte_SHT30>{luft_sht}%Rel</Luftfeuchte_SHT30>
    <Temperatur_Sensor>{temp_sen}C</Temperatur_Sensor>
</sensordaten>""".format(
        time     = timestamp,
        boden    = boden_feuchte(),
        temp_sht = sht_temp(),
        luft_sht = sht_humidity(),
        temp_sen = temperatur2()
    )

    with open("website/data/data.xml", "w") as f:
        f.write(xml)