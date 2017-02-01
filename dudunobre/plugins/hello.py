#coding: UTF-8
import re
import slackbot_settings
from dudunobre import doodle
from slackbot.bot import respond_to
from slackbot.bot import listen_to

def template_mail_secu(date, place, participants):
    (placename, additionnal_message) = slackbot_settings.PLACES[place]
    all_participants = map(lambda p: slackbot_settings.PARTICIPANTS[p.encode('utf-8')], participants) + slackbot_settings.DEFAULT_PARTICIPANTS.values()
    internal_participants = map(lambda i: i['name'], filter(lambda p: p['is_internal_resource'] == True, all_participants))
    external_participants = map(lambda i: i['name'], filter(lambda p: p['is_internal_resource'] == False, all_participants))

    return slackbot_settings.TEMPLATES['mail_secu']() % (
        date.strftime("%A %d %B"),
        placename,
        '\n'.join(internal_participants),
        '\n'.join(external_participants),
        additionnal_message
    )

def template_mail_booking(date):
    return slackbot_settings.TEMPLATES['mail_booking']() % (
        date.strftime("%A %d %B")
    )


@respond_to('e alegre$', re.IGNORECASE)
def greeting_message(message):
    message.reply(slackbot_settings.TEMPLATES['samba']())

@respond_to('samba$', re.IGNORECASE)
def samba(message):
    message.reply('https://www.youtube.com/watch?v=LTqnUudZTME')

@respond_to('^qui a rempli le doodle', re.IGNORECASE)
def who_filled_doodle(message):
    message.reply('hmm, je regarde')
    message.reply('\n'.join(doodle.participants()))

@respond_to('^repet', re.IGNORECASE)
def next_training(message):
    message.reply('atta, je regarde')
    (found_index, date, participants) = doodle.next_training()
    if found_index >= 0:
        message.reply('prochaine répèt le %s à 19h30' % date.strftime("%d/%m/%Y"))
        message.reply('on sera %s :' % len(participants))
        message.reply('\n'.join(participants))
    else:
        message.reply('pas de répèt prévu prochainement')

@respond_to('^mail r.p.t (.*)', re.IGNORECASE)
def mail_secu(message, place):
    message.reply('2 sec, je check le doodle')
    (found_index, date, participants) = doodle.next_training()
    if found_index >= 0:
        message.reply(template_mail_secu(date, place.strip(), participants))
    else:
        message.reply('euh, t\'es sûr qu\'il y a répèt cette semaine-là ?')


@respond_to('^mail r.s[a(ervation)]', re.IGNORECASE)
def mail_booking(message):
    message.reply('2 sec, je check le doodle')
    (found_index, date, participants) = doodle.next_training()
    if found_index >= 0:
        message.reply(template_mail_booking(date))
    else:
        message.reply('euh, t\'es sûr qu\'il y a répèt cette semaine-là ?')

