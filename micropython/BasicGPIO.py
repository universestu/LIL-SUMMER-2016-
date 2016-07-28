import time
import machine
pinOut = machine.Pin(5, machine.Pin.OUT)
def toggle(p):
    p.value(not p.value())
    time.sleep_ms(500)
    p.value(not p.value())
    time.sleep_ms(500)
    
toggle(pin)


pinIn = machine.Pin(4, machine.Pin.IN)
if pin.value():
    print('start....')
else:
    print('stop....')
    
