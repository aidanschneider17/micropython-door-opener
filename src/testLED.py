import networkSetup
from machine import Pin
import utime
import socket

ntwk = networkSetup.networkManager()

connected, ip = ntwk.connect('TP-Link_F6BD', '73937098')

if connected:
    print(ip)
    
    led = Pin('LED', Pin.OUT)

    data_socket = networkSetup.getSocket(2147, 5)

    while True:
        data = data_socket.recv(100)

        if data == b'TURN ON':
            led.value(1)
        elif data == b'TURN OFF':
            led.value(0)
        else:
            data_socket.close()
            break
    
else:
    print('Could not connect')
    
ntwk.disconnect()

