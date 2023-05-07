import RPi.GPIO as GPIO
import Menu as m
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)


def menuUp():
    NotImplemented           
def menuDown():
    NotImplemented

def menuSel():
    NotImplemented







def CheckButtons():
    if(GPIO.input(5)):
       menuSel()
    elif(GPIO.input(6)):
        menuUp()
        m.updateMenu()
        sleep(0.2)
    elif(GPIO.input(13)):

        NotImplemented   
m._Init_()
m.inSubM = False
m.MenuPos = 1
m.updateMenu()
m.setActive()        
while True:
    CheckButtons()        