import socket
import time

GET = 'update?key=E5JNXV8S63PYUUCW'
host = 'data.learninginventions.org'
addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)
s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (GET+'&'+f1+'='+v1+'&'+f2+'='+v2, host), 'utf8'))  #HTTP GET
print(GET+'&'+f1+'='+v1+'&'+f2+'='+v2)                    #parameter = update?key=E5JNXV8S63PYUUCW&field1=875&field2=795
time.sleep(1)                                   #keep wait or do something before s.close()
s.close()



import network
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
