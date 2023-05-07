import sevensegdisplay as seg7
import lcddisplay as lcd
from time import sleep
import os

MenuPos = 0
MenuMax = 5
inSubM = False
SubMPos = 0
SubMMax = 1
Clock_Version = "Experimental"
Active = True

InactivityDuration = 0 #in Seconds
InactivityDurationMax = 120
Timer_Hour = 0#in 24h format
Timer_Minute = 0#in Seconds

def _Init_ ():
   lcd.Toggle(True)
   lcd.print("Raspberry Pi 4\n\rVer:")
   sleep(0.2)
   lcd.print(Clock_Version)
   sleep(2)
   lcd.clear()
   lcd.Toggle(False)
   
#Setters
def setMenuPos(value):
    global MenuPos
    MenuPos = value
def setSubMPos(value):
    global SubMPos
    SubMPos = value
def setActive():
    global Active
    Active = True        
    
#Gettters      
def getMenuPos():
    return MenuPos
def getSubMPos():
    return SubMPos
def getActive():
    return Active
def getMenuMax():
    return MenuMax
def getSubMMax():
    return SubMMax
def getInSubM():
    return inSubM
   
#Graphics    
def updateMenu():
    if(Active):
        lcd.clear()
        lcd.Toggle(True)
        if(inSubM == False):
            if MenuPos == 1:
                lcd.print("\rSet Alarm <-  Page:1" + "\r\nRestart" + "\r\nShutdown" + "\r\nInactivity")
            elif MenuPos == 2:
                lcd.print("\rSet Alarm     Page:1" + "\r\nRestart <-" + "\r\nShutdown" + "\r\nInactivity")
            elif MenuPos == 3:
                lcd.print("\rSet Alarm     Page:1" + "\r\nRestart" + "\r\nShutdown  <-" + "\r\nInactivity")
            elif MenuPos == 4:
                lcd.print("\rSet Alarm      Page1:" + "\r\nRestart" + "\r\nShutdown" + "\r\nInactivity   <-")
            elif MenuPos == 5:
                lcd.print("\rExit <- Page:2")


        elif(inSubM == True):

            if MenuPos == 1:
                if SubMPos == 0:
                    lcd.print("\rSet Alarm:\n\r\n\r Hour: ")
                    lcd.print(str(Timer_Hour))
                    lcd.print("< Min: ")
                    lcd.print(str(Timer_Minute))
                    lcd.print("\r\n        <->")
                elif SubMPos == 1:
                    lcd.print("\rSet Alarm:\n\r\n\r Hour: ")
                    lcd.print(str(Timer_Hour))
                    lcd.print("  Min: ")
                    lcd.print(str(Timer_Minute))
                    lcd.print("<\r\n        <->")
                else:
                    print("Error", '"', SubMPos, '"', "Is no valid SubM Position")                    


            elif MenuPos == 2:
                if SubMPos == 0:
                    lcd.print("\rRestart\n \r\n    JES<-    NO")
                elif SubMPos == 1:
                    lcd.print("\rRestart\n \r\n    JES      NO<-")    
                else:
                    print("Error", '"', SubMPos, '"', "Is no valid SubM Position")            

            elif MenuPos == 3:
                lcd.print("\rSet Duration:\n\r\n\r     <- ")
                lcd.print(str(InactivityDuration))
                lcd.print(" ->  Sec.")            

            elif MenuPos == 4:
                if SubMPos == 0:
                    lcd.print("\rShutdown\n \r\n    JES<-    NO")
                elif SubMPos == 1:
                    lcd.print("\rShutdown\n \r\n    JES      NO<-")    
                else:
                    print("Error", '"', SubMPos, '"', "Is no valid SubM Position")                        
            elif MenuPos == 5:
                if SubMPos == 0:
                    lcd.print("\rExit\n \r\n    JES<-    NO")
                elif SubMPos == 1:
                    lcd.print("\rExit\n \r\n    JES      NO<-")    
                else:
                    print("Error", '"', SubMPos, '"', "Is no valid SubM Position")               
        else:
            print("Error", inSubM, "Is no valid State")
#Functions                        
        
def Restart():
    lcd.print("\r|Rebooting...|")
    sleep(2)
    lcd.Toggle(False)
    seg7.setBrightness(0)
    sleep(1)
    os.system("sudo reboot")        
        
def Shutdown():
    lcd.print("\r|Shutting Down...|")
    sleep(2)
    lcd.Toggle(False)
    lcd.clear()
    seg7.setBrightness(0)
    sleep(1)
    os.system("sudo reboot")     

def Exit():
    lcd.Toggle(False)
    lcd.clear()           
        
def SetInactivity():
    if InactivityDuration < InactivityDurationMax:
        InactivityDuration += 1
    else:
        InactivityDuration = 0
def SetTimer(hour_min):
    if hour_min == "hour":
        if Timer_Hour < 24:
            Timer_Hour += 1
        else:
            Timer_Hour = 0       
    elif hour_min == "min":
        if Timer_Minute < 60:
            Timer_Minute += 1
        else:
            Timer_Minute = 1    
            
        
                                                  

