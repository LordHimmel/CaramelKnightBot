import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop

"""
After **inserting token** in the source code, run it:

```
$ python2.7 diceyclock.py
```

[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:

- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = str(msg['text']).lower()

    print ('Got command: %s' % command)

    if command.find('кинь д6')>=0:
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/help' or command.find( "помоги")>=0 :
        bot.sendMessage(chat_id,"Я еще пока маленькая и почти ничего не умею. \nМогу кидать д6 и говорить сколько времени.\nТерпеть не могу ваху и считаю Даню пидором")
    elif command.find('врем')>=0:
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command.find('карамель')>=0:
        bot.sendMessage(chat_id, "Мур мур мур")

    elif command.count("ваха")>0 :
        bot.sendMessage(chat_id, "Вархаммер говно")

    elif command.find("люблю")>=0 :
        bot.sendMessage(chat_id,"А Я Папу и Маму люблю")
    else:
        bot.sendMessage(chat_id,"Помочь?")


bot = telepot.Bot("500928095:AAF-GXdlcIZwHKM4z2iS7LiEx2u_K3YKLr4")

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
