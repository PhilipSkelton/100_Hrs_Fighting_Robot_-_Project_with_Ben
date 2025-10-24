import gpiozero
import time


button = gpiozero.Button(17)
led = gpiozero.LED(4)

while True:
        if button.is_pressed:
                print("1")
                led.on()
        else:
                print("0")
                led.off()

# test change 3

