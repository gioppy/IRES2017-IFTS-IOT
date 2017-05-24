import RPi.GPIO as GPIO
# import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# RGB
chan_list = [11,13,15]
GPIO.setup(chan_list, GPIO.OUT, initial=GPIO.LOW)
'''
GPIO.output(chan_list, GPIO.HIGH)

time.sleep(10)

GPIO.output(chan_list, GPIO.LOW)
GPIO.cleanup(chan_list);
'''
r = GPIO.PWM(chan_list[0], 100)
g = GPIO.PWM(chan_list[1], 100)
b = GPIO.PWM(chan_list[2], 100)

r.start(0)
g.start(0)
b.start(0)

def setColor(rgb = []):
  rgb = [(x / 255.0) * 100 for x in rgb]
  r.ChangeDutyCycle(rgb[0])
  g.ChangeDutyCycle(rgb[1])
  b.ChangeDutyCycle(rgb[2])

def rgbCleanup():
  GPIO.output(chan_list, GPIO.LOW)
  GPIO.cleanup(chan_list)