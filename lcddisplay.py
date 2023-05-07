from RPLCD.i2c import CharLCD

from time import sleep

lcd = CharLCD('PCF8574', 0x27)

def print(Input):
    lcd.write_string(Input)
    
def Toggle(toggle):
    if toggle == True:
        lcd.backlight_enabled = True
    elif toggle == False:
        lcd.backlight_enabled = False
    else:
        print("Error:",  '"', toggle, '"', "is not valid")     

def printime(hour, minute, second):

    if second < 10:
        if minute < 10:
            if hour < 10:
                    lcd.write_string("\nTIME:" + "0" + str(hour) + ":" + "0" + str(minute) + ":" + "0" + str(second))
            else:
                lcd.write_string("\nTIME:" + str(hour) + ":" + "0" + str(minute) + ":" + "0" + str(second))
        else:
            lcd.write_string("\nTIME:" + str(hour) + ":" + str(minute) + ":" + "0" + str(second))

            
    else:
        if minute < 10:
            if hour < 10:
                    lcd.write_string("\nTIME:" + "0" + str(hour) + ":" + "0" + str(minute) + ":" + str(second))
            else:
                lcd.write_string("\nTIME:" + str(hour) + ":" + "0" + str(minute) + ":" + str(second))
    
        else:
            if hour < 10:
                lcd.write_string("\nTIME:" + "0" + str(hour) + ":" + str(minute) + ":" + str(second))

            else:
                lcd.write_string("\nTIME:" + str(hour) + ":" + str(minute) + ":" + str(second))


            
        

def printnexttimer(hour, minute):
    if minute < 10:
        lcd.write_string("\nNexEv:" + str(hour) + ":" + "0" + str(minute))

    else:
        lcd.write_string("\nNexEv:" + str(hour) + ":" + str(minute))


def printMain(hour, minute, second, hour_timer, minute_timer):
    printime(hour, minute, second)
    lcd.crlf()
    printnexttimer(hour_timer, minute_timer)

def clear():
    lcd.clear()