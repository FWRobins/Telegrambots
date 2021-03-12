##I made this so I can quickly send a file to my cellphone
##without having to emeil or log into whatappweb ect


# import requests
# from bs4 import BeautifulSoup
# import datetime
import telegram
# import time
import pyautogui

my_token = # removed for security purposed
chatid = # chat id to whom to send the file

##get file name from user
myfile =  pyautogui.prompt(text='File name?', title='Card Name', default='')
myfile = myfile[1:-1]

def send(myfile, chat_id, token=my_token):
	bot = telegram.Bot(token=token)
	bot.sendDocument(chat_id=chat_id, document=open(myfile, 'rb'), timeout=100000)


send(myfile, chatid)
