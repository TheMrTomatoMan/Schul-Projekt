import machine
import time

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)



def temperatur2():
    data= i2c.readfrom_mem(0x48, 0x00, 2)

    raw = (data[0] << 8) | data[1]
    raw = raw >> 5
    temp = raw * 0.125
    temp = round(temp, 1)
    return temp