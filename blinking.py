import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
for i in range(10):
         GPIO.output(7,True)
         print("LED IS FINALLY ON")

         time.sleep(1)

         GPIO.output(7,False)
         print("LED IS OFF")

         time.sleep(1)
print("PROGRAM COMPLETE!")
GPIO.cleanup()
               
