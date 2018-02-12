import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
from content import conversate
from commands import calculate

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

    if command[0]!='/':
        try:
            bot.sendMessage(chat_id,conversate(command))
        except:
            pass
    else: 
        try:
            bot.sendMessage(chat_id,calculate(command))
        except:
            pass
   


bot = telepot.Bot("500928095:AAF-GXdlcIZwHKM4z2iS7LiEx2u_K3YKLr4")

MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
