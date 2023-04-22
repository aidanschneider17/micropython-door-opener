from motor import dcmotor
from mfrc522 import MFRC522
from machine import Pin
from passwordManager import pswdManager
import utime

motor = dcmotor(6,7)
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

def main():
    master = 2855651907
    add_key = 2846667955
    delete_key = 2854203507

    manager = pswdManager(master)

    while True:
        
        card = get_key()

        if manager.contains(card, master):
            open_door()
        
        elif card == add_key:
            utime.sleep_ms(500)
            add_card(master, manager)
        
        elif card == delete_key:
            utime.sleep_ms(500)
            delete_card(master, manager)
            

        

def get_key():
    got = True

    while got:
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card = int.from_bytes(bytes(uid),"little",False)
                got = False

    return card


def open_door():
    motor.motorMove(1)
    utime.sleep(2.5)
    motor.stop()
    utime.sleep(1)
    motor.motorMove(-1)
    utime.sleep(2.5)
    motor.stop()


def add_card(master, manager):
    
    success = True

    master_test = get_key()
    print(master_test)

    if master_test == master:
        utime.sleep_ms(500)
        success = manager.add_password(get_key(),master)
        


def delete_card(master, manager):


    success = True

    

    master_test = get_key()
    print(master_test)

    if master_test == master:
        utime.sleep(0.5)
        deleted = get_key()
        print(deleted)

        success = manager.delete_password(deleted,master)
        


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
    
        motor.stop()



