import machine

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
devices = i2c.scan()
print("test")
if len(devices) == 0:
    print("No I2C device found!")
else:
    print('I2C devices found:', [hex(device) for device in devices])