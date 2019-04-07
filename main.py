import time
import socket
import network

from settings import socket_port, sensor_list, wifi_settings
from machine import Pin


# Connect to the WiFi network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
if "ifconfig" in wifi_settings:
    sta_if.ifconfig(wifi_settings["ifconfig"])
sta_if.connect(wifi_settings["ssid"], wifi_settings["password"])
while not sta_if.isconnected():
    pass

# Setup network socket
s = socket.socket()
addr = socket.getaddrinfo('0.0.0.0', socket_port)[0][-1]
s.bind(addr)
s.listen(1)

# Initialize sensor dictionary
sensors = {}

# Setup sensors
for sensor in sensor_list:
    sensors[sensor] = Pin(sensor, Pin.IN)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    pin = int(cl.recv(100))

    if pin in sensors:
        print(sensors[pin].value())
        cl.send(str(sensors[pin].value()))
    else:
        cl.send("False")
