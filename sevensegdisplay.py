
import RPi.GPIO as GPIO
import tm1637 as tm1637


display = tm1637.TM1637(clk=(23), dio=(24))
display.brightness(5)
def update7seg(hour, minute):
    display.numbers(hour, minute)

def setBrightness(brightness):
    display.brightness(brightness)