# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import requests
import json
import slackbot_settings

def doodle():
  regex = r"doodleJS.data, {\"poll\":(.*)}\);"
  test_str = requests.get(slackbot_settings.DOODLE_URL).text
  matches = re.search(regex, test_str, re.MULTILINE)
  return json.loads(matches.group(1))

def participants():
  return map(lambda x: x['name'], doodle()['participants'])
