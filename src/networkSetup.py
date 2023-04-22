import network
import socket
import time

class networkManager():
    
    def __init__(self):
        
        self.wlan = network.WLAN(network.STA_IF)
    
    def connect(self, ssid, password):
        
        self.wlan.active(True)
        print(self.wlan.scan())
        self.wlan.connect(ssid, password)
        
        while not self.wlan.isconnected():
            time.sleep_ms(50)
        
        return (self.wlan.isconnected(), self.wlan.ifconfig()[0])
    
    def disconnect(self):
        self.wlan.disconnect()
        self.wlan.active(False)
        
    def scan(self):
        return(self.wlan.scan())
    
    
def getSocket(port, num_clients):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('',port))

    server_socket.listen(num_clients)


    data_socket, address = server_socket.accept()
    
    server_socket.close()
    
    return data_socket
