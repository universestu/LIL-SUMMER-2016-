# micropython-project

ตั้งค่า password ของ websocket

passwd1 = '1234'

with open("port_config.py", "w") as f:

        f.write("WEBREPL_PASS = %r\n" % passwd1)
   
เชื่อมต่อ wifi     

import network

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)

sta_if .connect('ssid','pass')


เปิดใช้งาน webrepl

import webrepl

webrepl.start()

esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=8m 0 esp8266-2016-05-03-v1.8.bin 

nodemcu // esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=8m -fm dio 0 esp8266-2016-05-03-v1.8.bin

esptool.py --port COM7 erase_flash 

