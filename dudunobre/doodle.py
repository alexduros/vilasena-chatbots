# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import requests
import json
import slackbot_settings
import logging
import datetime

def doodle():
  regex = r"doodleJS.data, {\"poll\":(.*)}\);"
  test_str = requests.get(slackbot_settings.DOODLE_URL).text
  matches = re.search(regex, test_str, re.MULTILINE)
  doodle = json.loads(matches.group(1))
  logging.debug(json.dumps(doodle, indent=4, sort_keys=True))
  return doodle

def participants():
  return map(lambda x: x['name'], doodle()['participants'])

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def next_training():
  t = next_weekday(datetime.datetime.today(), 1)
  doodle_format = "Tue %s/%s/%s" % (t.month, t.day, t.year - 2000)
  logging.debug('doodle_format: %s' % doodle_format)
  try:
    day_index = doodle()['optionsText'].index(doodle_format)
    logging.debug('found_index: %s' % day_index)
    return (day_index, t)
  except Exception as e:
    logging.error('error_doodle_today: %s' % e)
    return (-1, None)
