# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
import time
from hygrometer import boden_feuchte
gc.collect()

while True:
    print(f"Boden Feuchte: {boden_feuchte()}%")
    time.sleep(5)