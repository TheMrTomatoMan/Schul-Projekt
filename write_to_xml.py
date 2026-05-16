from thermometer import temperatur2
from sht30_output import sht_temp, sht_humidity
from hygrometer import boden_feuchte

def xml_write():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<sensordaten>
    <Boden_Feuchtigkeit>{boden}%</Boden_Feuchtigkeit>
    <Temperatur_SHT30>{temp_sht}C</Temperatur_SHT30>
    <Luftfeuchte_SHT30>{luft_sht}%Rel</Luftfeuchte_SHT30>
    <Temperatur_Sensor>{temp_sen}C</Temperatur_Sensor>
</sensordaten>""".format(
        boden    = boden_feuchte(),
        temp_sht = sht_temp(),
        luft_sht = sht_humidity(),
        temp_sen = temperatur2()
    )

    with open("data.xml", "w") as f:
        f.write(xml)