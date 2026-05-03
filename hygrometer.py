import machine
import time

pin = machine.ADC(0)  


def boden_feuchte():
    # Kalibrierungswerte
    wet = 800
    dry = 200
    
    #Output between 0-1024
    voltage = pin.read()
    
    value = (voltage - dry) / (wet - dry) * 100
    #umrechnung in %
    prozent = max(0, min(100, value))
    prozent = round(prozent,1)
    return prozent