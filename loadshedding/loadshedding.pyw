##This files main purpose is to check the scheduled rolling blackout times

import pandas as pd
from datetime import datetime as dt
from datetime import date


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


my_token = #removed for security purposes

updater = Updater(my_token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

##these are just some tutorial and test command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Im a bot plz talk to me")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update, context):
    msg = update.message.text
    if 'Hello' in msg[:5]:
        msg2 = "Hello "+ str(update.message.from_user.first_name)
        context.bot.send_message(chat_id=update.effective_chat.id, text=msg2)

echo_handler = MessageHandler(Filters.text &(~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def caps(update, context):
    text_caps = " ".join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def chatid(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(update.message))

chatid_handler = CommandHandler('chatid', chatid)
dispatcher.add_handler(chatid_handler)

def calc(update, context):
    msg = update.message.text[6:]
    rep = {'×':'*', '÷':'/', '^':'**', '(':'*('}
    for x, y in rep.items():
        msg = msg.replace(x, y)
    msg = eval(msg)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

calc_handler = CommandHandler('calc', calc)
dispatcher.add_handler(calc_handler)

#command stuctured as /ls_schedule gbay 4
#command will check the .csv file and return the timeslots
#of the blackouts for the region (eg gbay or swes)
#matched the level (eg 1,2,3 or 4) for the day
def ls_schedule(update, context):
    region = update.message.text[-6:-2]
    ls_stage = int(update.message.text[-1])
##    print(region)
##    print(ls_stage)
    today = date.today().day
    mycolumns = [0, 1, today+1]
    gbfile = pd.read_csv(f"{region}.csv", usecols = mycolumns, names=["START", "END", "DATE"])
    gbfile = gbfile.drop(0)
    filter = gbfile[(gbfile.DATE <= ls_stage) & (gbfile.DATE != 0)]
    qty_rows = range(len(filter))
    msg = ""
    for row in qty_rows:
        msg += f"{filter.iloc[row].START}, {filter.iloc[row].END}\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

ls_schedule_handler = CommandHandler('ls_schedule', ls_schedule)
dispatcher.add_handler(ls_schedule_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")



unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
