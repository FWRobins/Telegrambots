##I used to play alot of Warframe and wrote this script to continually
##check if there has been a update.

import requests
from bs4 import BeautifulSoup
import datetime
import telegram
import time

#scrape website to check if a new update has been released
def updatecheck():
    data_base = requests.get('https://forums.warframe.com/forum/3-pc-update-notes/')
    data = data_base.content
    soup = BeautifulSoup(data, "html.parser")
    all = soup.find_all("ol")
    all_li = all[0].find("time")
    datestr = all_li.get("datetime").replace("Z","").replace("T", " ")
    datestamp = datetime.datetime.timestamp(datetime.datetime.strptime(datestr,"%Y-%m-%d %H:%M:%S"))
    diff = datetime.datetime.timestamp(datetime.datetime.now())-datestamp
    return diff


my_token = # removed for security purposes
chatid = # user chat id that should receive the notification
def send(msg, chat_id, token=my_token):
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)


send("Warframe updater running", chatid)

##main loop to check if update has been added after previous check
while True:
    try:
        if updatecheck() < 18000:
            send("New Warframe Update Available", chatid)
    except:
        pass
    time.sleep(18000)
