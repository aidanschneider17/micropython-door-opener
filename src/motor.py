from machine import Pin

class dcmotor:

    def __init__(self, cwPin, ccwPin):
        self.cw = Pin(cwPin, Pin.OUT)
        self.ccw = Pin(ccwPin, Pin.OUT)

    def motorMove(self, direction):
        
        if direction < 0:
            self.cw.value(0)
            self.ccw.value(1)
        elif direction == 0:
            self.cw.value(0)
            self.ccw.value(0)
        else:
            self.cw.value(1)
            self.ccw.value(0)
            
    def stop(self):
        self.cw.value(0)
        self.ccw.value(0)



