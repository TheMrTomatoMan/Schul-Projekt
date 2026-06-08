# Importiert alle benötigten Librarys
from hygrometer import boden_feuchte
from sht30_output import sht_humidity, sht_temp
from thermometer import temperatur2
import time

# eine Funktion
def json_write():
# Definiert "t" als Aktuelle Zeit (die der Microcontroller hat) im 24h vormat
    t = time.localtime()
    timestamp = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])
# ich benutze kein json.dumps damit ich mit einer einfachen änderung den selben code auch für XML nutzen kann
# Schreibt eine Variable mit zeilenumbrüchen
    json_str = (
        '{{\n'
        '  "Time": "{}",\n'
        '  "Temperatur von SHT30": "{}",\n'
        '  "Luftfeuchte von SHT30": "{}",\n'
        '  "Temeratur von Sensor": "{}",\n'
        '  "Boden Feuchtigkeit": "{}"\n'
        '}}'
# Setzt die Werte in den Sting ein
    ).format(
        timestamp,
        "{}°C".format(sht_temp()),
        "{}%Rel".format(sht_humidity()),
        "{}°C".format(temperatur2()),
        "{}%".format(boden_feuchte())
    )
# Überschreibt die data.json mit dem neuen string
    with open("website/data/data.json", "w") as f:
        f.write(json_str)