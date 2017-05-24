'''
Required packages:
- I2C Interface: http://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/
- Telegram Bot: https://github.com/python-telegram-bot/python-telegram-bot
- SMBus (python3-smbus): http://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/
'''

from telegram_bot import TGBot

if __name__ == '__main__':
  try:
    bot = TGBot()
  except KeyboardInterrupt:
    pass
  finally:
    bot.cleanup()