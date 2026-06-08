# Importiert die maschine library
import machine
# Setzt den Analogen Output auf Pin 0 der variable "pin"
pin = machine.ADC(0)  

# Eine Funktion die die Bodenfeuchtigkeit in % ausgibt und auf eine nachkommastelle rundet
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