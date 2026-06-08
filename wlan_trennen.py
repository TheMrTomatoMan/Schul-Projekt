# Importiert die network Library
import network

# Eine Funktion die das Wlan wenn es Aktiv ist einmal Disconectet 
def wlan_trennen():
    wlan = network.WLAN(network.STA_IF)
    if wlan.active(True):
        wlan.disconnect()
        wlan.active(False)