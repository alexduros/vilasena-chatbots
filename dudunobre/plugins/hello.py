#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('e alegre$', re.IGNORECASE)
def greeting_message(message):
    message.reply('''
E COLORIDA,

FALO DE QUEM ?

DA BATERIA VILA SENA !
    ''')

@respond_to('samba$', re.IGNORECASE)
def samba(message):
    message.reply('https://www.youtube.com/watch?v=LTqnUudZTME')
