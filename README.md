# My Telegram Bots

Just some Telegram bots I use.

## Load-shedding aka Rolling black outs

This Scripts main purpose is to check the scheduled rolling blackout times

### Prerequisites

The schedules are local files in the same directory as the script.
These I downloaded in CSV format from our local municipality site.
You need to create your own bot in Telegram first from BotFather
and get you API token.
Add this token under 'my_token'

## Send File

I made this so I can quickly send a file to my cellphone
without having to email or log into Whatsapp-web ect.

### Prerequisites

Pyautogui will request the file location from the user and remove the starting end ending quotes.
The script wil then use your API Token and chit_id to send it to you.
You need to create your own bot in Telegram first from BotFather
and get you API token.
Add this token under 'my_token'
And start a chat with your bot so that a chat_id can be generated.
the 'loadshedding' script has a method chatid() that can be used to get this.

## Warframe Update Check

I used to play alot of Warframe and wrote this script to continually check if there has been a update.

### Prerequisites

This check the PC patch notes page for any new posts and then send a notification.
You need to create your own bot in Telegram first from BotFather
and get you API token.
Add this token under 'my_token'
And start a chat with your bot so that a chat_id can be generated.
the 'loadshedding' script has a method chatid() that can be used to get this.
