import network

def wlan_trennen():
    wlan = network.WLAN(network.STA_IF)
    if wlan.active(True):
        wlan.disconnect()
        wlan.active(False)