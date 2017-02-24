import telepot
import time
import string
import re
import requests
from random import randint
from pprint import pprint
from io import BytesIO
#from LogErrors import MakeLog


g_url = 'https://www.google.it/search?q=coscia+di+pollo&espv=2&biw=1707&bih=818&source=lnms&tbm=isch&sa=X&ved=0ahUKEwid0-zs4anSAhUHVxQKHSgOC4cQ_AUIBigB'

r = requests.get(g_url, stream=True)
r = r.content
#r is now my html code

#r = r.decode("utf-8")

pattern = '<img .+?>'

try:
    found = re.findall(pattern, str(r))
except AttributeError:
    found = ''

pattern = 'src=\"(.+?)\"'

found = re.findall(pattern, str(r))

print(len(found))

for i, val in enumerate(found):
  if str(re.search('https', val))=='None':
    del found[i]

def handle(msg):
  global found
  content_type, chat_type, chat_id = telepot.glance(msg)

  chat_id = msg['chat']['id']
  command_input = msg['text']

  #print(chat_id, content_type, chat_type)

  #response = bot.getUpdates()

  #pprint(msg)

  bot.sendMessage(chat_id, 'Ciao Andò')
  bot.sendPhoto(chat_id, found[randint(0,len(found))])

bot = telepot.Bot('247025363:AAHdRykgnCXdP3Lb6INVADAs0r5RNlF7LbY')

bot.message_loop(handle)

print("I'm Working Master.")

while 1:
  time.sleep(10)
