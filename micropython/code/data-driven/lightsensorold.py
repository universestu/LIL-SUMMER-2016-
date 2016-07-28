import machine
import time
import socket
import esp
import network

pin = machine.Pin(5, machine.Pin.OUT)
def toggle(p):
    p.value(not p.value())
    time.sleep_ms(500)
    p.value(not p.value())
    time.sleep_ms(500)

def connectsend():
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True)       
    wlan.scan()            
    wlan.isconnected()      
    wlan.connect('gogo_mt', 'ilovecpeilovecpe')    
    wlan.ifconfig() 
    GET = 'update?key=SPOA89HOE84P6NXJ&field1='
    host = 'data.learninginventions.org'
    addr = socket.getaddrinfo(host, 80)[0][-1]
    adc = machine.ADC(0)
    value = '0'
    i=0
    while wlan.isconnected():
        value = str(adc.read())
        s = socket.socket()
        s.connect(addr)
        s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (GET+value, host), 'utf8'))
        toggle(pin)
        s.close()
        print(value)
        i+=1
        print('---',i)
        time.sleep(15)
    machine.reset()

def main():
    try:
        connectsend()
    except:
        import machine
        machine.reset()

        



    
