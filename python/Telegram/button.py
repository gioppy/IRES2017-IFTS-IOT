import RPi.GPIO as GPIO

class ButtonBot:
  def __init__(self, cb):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(16, GPIO.FALLING, callback=cb)

    '''
    try:
      GPIO.wait_for_edge(16, GPIO.FALLING)
      cb()
    except KeyboardInterrupt:
      pass
    finally:
      self._cleanup()
    '''
    pass

  def cleanup(self):
    GPIO.cleanup(16)
    GPIO.remove_event_detect(16)