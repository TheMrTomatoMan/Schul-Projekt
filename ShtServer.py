import ESP8266WebServer as server
from WifiConnect import wifiConnect
import network
import machine
from sht30 import SHT30

# Sensor einbinden und initialisieren
sensor = SHT30()

# Wi-Fi configuration
#ssid = "<ssid>"
#password = "<password>"

#Schule 
ssid = "gsog-iot"
password = "IOT_Projekt_BFK-S_2022"



wifiConnect(ssid, password)

# Liefert CSS fuer Webseite
def get_css():
    css = """
        <style>
         body {
            background-color: #cccccc;
            font-family: Arial, Helvetica, Sans-Serif;
            Color: #000088;
         }
         </style>"""  
    return css
        
def handleRoot(socket,args):
#    print("in handleRoot")
    temperature, humidity = sensor.measure()
    page = """
        <!DOCTYPE HTML>
        <html>
        <head>
         <title>HTML Demo</title>
         {0}
        </head>
        <body>
          <h1>Hallo Wemos D1 mini</h1>
          <p>Temperatur: {1} &deg;</p>
          <p>Feuchtigkeit: {2} %</p>
        </body>
        </html>
        """.format(get_css(),round(temperature,1),round(humidity,1))
    server.ok(socket,"200","text/html",page)
    
def handlePlainTemperatur(socket,args):
#    print("in plainTemperatur)
    temperature, humidity = sensor.measure()
    server.ok(socket,"200",str(temperature))

def handleOnNotFound(socket):
#    print("in onNotFound")
    server.err(socket,"404","File Not Found")

server.begin()
server.onPath("/", handleRoot)
server.onPath("/plainTemperatur", handlePlainTemperatur)
#server.onNotFound(handleOnNotFound)

try:
    while True:
        # Let server process requests
        server.handleClient()
except:
    server.close()
