import machine
import time

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)

print(i2c)

def temperatur2():
    data= i2c.readfrom(0x49, 1)

    value = int.from_bytes(data, 'big')
    return value

