# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
import time
from hygrometer import boden_feuchte
from sht30_output import sht_humidity, sht_temp
from thermometer import temperatur2
gc.collect()

'''while True:
    print(f"Boden Feuchte: {boden_feuchte()}%")
    print(f"Temperatur on Board: {sht_temp()}°C")
    print(f"Luftfeuchtigkeit on Board: {sht_humidity}% Rel")
    print(f"Temperatur an Temperatur sensor: {temperatur2}°C")
    time.sleep(5)'''