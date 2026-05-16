# This file is executed on every boot (including wake-boot from deepsleep)
import os, machine
import gc
gc.collect()

import ESP8266WebServer as server
from WifiConnect import wifiConnect
from write_to_json import json_write
from write_to_xml import xml_write
import time
 
SSID     = "gsog-iot"
PASSWORD = "IOT_Projekt_BFK-S_2022"
 
wifiConnect(SSID, PASSWORD)
 
def handleData(socket, args):
    try:
        with open("data.json", "r") as f:
            data = f.read()
        server.ok(socket, "200", "application/json", data)
    except:
        server.err(socket, "404", "data.json not found")
 
server.setDocPath("/Website/")
server.onPath("/data", handleData)
server.begin(80)
 
last_update = 0
 
try:
    while True:
        server.handleClient()
 
        # Sensordaten alle 10 Sekunden neu schreiben
        if time.time() - last_update >= 10:
            json_write()
            xml_write()
            last_update = time.time()
except:
    server.close()