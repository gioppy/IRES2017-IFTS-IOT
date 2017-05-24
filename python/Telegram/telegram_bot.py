from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ForceReply, ReplyKeyboardMarkup, KeyboardButton
from button import ButtonBot
import logging, sqlite3, temp_sensor, lcd_i2c, rgb

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class TGBot:
  MENU, AWAIT_CONFIRMATION, AWAIT_INPUT = range(3)
  state = dict()
  context = dict()

  def _btn(self, channel):
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT * FROM Users')
    rows = cur.fetchall()
    for row in rows:
      chat_id = row[0]
      user_name = row[1]
      self.bot.sendMessage(chat_id, text="Hey you {}!".format(user_name))
      #print('{} {}'.format(chat_id, user_name))

  def __init__(self):
    # connect to db
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Users (TOKEN string, NAME string)')
    con.commit()
    con.close()

    # Create the EventHandler and pass it your bot's token.
    # inserire l'ID del bot
    updater = Updater("...botID...")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    self.bot = dp.bot

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", self.start))
    dp.add_handler(CommandHandler("help", self.help))
    dp.add_handler(CommandHandler("temperature", self.temperature))
    dp.add_handler(CommandHandler("lcd", self.lcd))
    dp.add_handler(CommandHandler("lighton", self.lighton))
    dp.add_handler(CommandHandler("lightoff", self.lightoff))
    dp.add_handler(CommandHandler("lightchange", self.lightchange, pass_args=True))
    dp.add_handler(CommandHandler("subscribe", self.subscribe))
    dp.add_handler(CommandHandler("unsubscribe", self.unsubscribe))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], self.lcd))

    # log all errors
    dp.add_error_handler(self.error)

    # Start the Bot
    updater.start_polling()

    self.btn = ButtonBot(self._btn)

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

  def start(self, bot, update):
    bot.sendMessage(update.message.chat_id, text="Hi!")

  def help(self, bot, update):
    text = "Commands list:\n/temperature: get the temperature in this time\n/lcd: interact with LCD\n/lighton: turn on RGB Led\n/lightoff: turn off RGB Led\n/lightchange ... pass the rgb color to change (ex.: 0,0,255)\n/subscribe: ???\n/unsubscribe: ???"
    bot.sendMessage(update.message.chat_id, text=text)

  def temperature(self, bot, update):
    sensors = temp_sensor.setSensors()
    temps = temp_sensor.getTemperature(sensors)
    temp = float(temps[sensors[0]])
    bot.sendMessage(update.message.chat_id, text="Temperature is {}°".format(temp))

  def lcd(self, bot, update):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    chat_state = self.state.get(chat_id, self.MENU)
    chat_context = self.context.get(chat_id, None)
    text = update.message.text
    username = update.message.from_user.username

    if chat_state == self.MENU and text[0] == '/':
      self.state[chat_id] = self.AWAIT_INPUT
      self.context[chat_id] = user_id
      bot.sendMessage(chat_id, text="Please enter a phrase or /cancel to abort", reply_markup=ForceReply())
    elif chat_state == self.AWAIT_INPUT and chat_context == user_id:
      del self.state[chat_id]
      del self.context[chat_id]
      lcd_i2c.lcd_init()
      lcd_i2c.lcd_string(text, lcd_i2c.LCD_LINE_1)
      lcd_i2c.lcd_string('@{}'.format(username), lcd_i2c.LCD_LINE_2)

  def lighton(self, bot, update):
    rgb.setColor([255,255,255])
    bot.sendMessage(update.message.chat_id, text="Light on RGB")

  def lightoff(self, bot, update):
    rgb.setColor([0,0,0])
    bot.sendMessage(update.message.chat_id, text="Light off RGB")

  def lightchange(self, bot, update, args):
    rgb_str = args[0].split(',')
    rgb_num = [int(x) for x in rgb_str]
    rgb.setColor(rgb_num)
    bot.sendMessage(update.message.chat_id, text="Change color to {0}".format(rgb_str))

  def subscribe(self, bot, update):
    chat_id = update.message.chat_id
    user_name = update.message.from_user.name
    # print('{} : {}'.format(chat_id, user_name))
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT TOKEN FROM Users WHERE TOKEN=?', (chat_id,))
    rows = cur.fetchall()
    for row in rows:
      if row != None:
        bot.sendMessage(update.message.chat_id, text="You have already subscribed.")
        break
    else:
      bot.sendMessage(update.message.chat_id, text="You have successfully subscribed.")
      cur.execute('INSERT INTO Users VALUES(?, ?)', (chat_id, user_name))
    con.commit()
    con.close()

  def unsubscribe(self, bot, update):
    chat_id = update.message.chat_id
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('DELETE FROM Users WHERE TOKEN=?', (chat_id,))
    bot.sendMessage(update.message.chat_id, text="Bye!!!")
    con.commit()
    con.close()

  def error(self, bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

  def cleanup(self):
    # cleanup rgb
    rgb.rgbCleanup()
    # cleanup lcd
    lcd_i2c.lcd_byte(0x01, lcd_i2c.LCD_CMD)
    # cleanup button
    self.btn.cleanup()