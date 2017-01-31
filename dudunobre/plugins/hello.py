#coding: UTF-8
import re
import slackbot_settings
from dudunobre import doodle
from slackbot.bot import respond_to
from slackbot.bot import listen_to

def template_mail_secu(date, place, participants):
    (placename, additionnal_message) = slackbot_settings.PLACES[place]
    all_participants = map(lambda p: slackbot_settings.PARTICIPANTS[p], participants) + slackbot_settings.PARTICIPANTS.values()
    internal_participants = map(lambda i: i['name'], filter(lambda p: p['is_internal_resource'] == True, all_participants))
    external_participants = map(lambda i: i['name'], filter(lambda p: p['is_internal_resource'] == False, all_participants))

    return '''
Bonjour à tous,

Voici la liste des personnes présentes ce %s à la répétition de la batucada %s :

%s
Personnes extérieures à Canal+ :

%s

%s

Merci et bonne journée.

Alexandre
    ''' % (
        date.strftime("%A %d %B"),
        placename,
        '\n'.join(internal_participants),
        '\n'.external_participants,
        additionnal_message
    )


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
    (found_index, date, participants) = doodle.next_training()
    if found_index >= 0:
        message.reply('prochaine répèt le %s à 19h30' % date.strftime("%d/%m/%Y"))
        message.reply('on sera %s :' % len(participants))
        message.reply('\n'.join(participants))
    else:
        message.reply('pas de répèt prévu prochainement')

@respond_to('^mail répèt (.*)', re.IGNORECASE)
def samba(message, place):
    message.reply('2 sec, je check le doodle')
    (found_index, date, participants) = doodle.next_training()
    if found_index >= 0:
        message.reply(template_mail_secu(date, place, participants))
    else:
        message.reply('euh, t\'es sûr qu\'il y a répèt cette semaine-là ?')

