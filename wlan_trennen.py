import network

def wlan_trennen():
    wlan = network.WLAN(network.STA_IF)
    wlan.disconnect()
    wlan.active(False)