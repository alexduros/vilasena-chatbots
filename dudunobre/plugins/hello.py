#coding: UTF-8
import re
from dudunobre import doodle
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

@respond_to('^qui a rempli le doodle', re.IGNORECASE)
def samba(message):
    message.reply('hmm, je regarde')
    message.reply('\n'.join(doodle.participants()))

@respond_to('^repet', re.IGNORECASE)
def samba(message):
    message.reply('atta, je regarde')
    (found_index, date) = doodle.next_training()
    if found_index >= 0:
        message.reply('prochaine répèt le %s à 19h30' % date.strftime("%d/%m/%Y"))
    else:
        message.reply('pas de répèt prévu prochainement')

