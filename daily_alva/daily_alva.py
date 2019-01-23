# -*- coding: utf-8 -*-
import csv
import daily_alva_config
import datetime
from datetime import date
import json
import os
import random
import requests

webhook = daily_alva_config.webhook
name_list = daily_alva_config.employees
company = daily_alva_config.company
slack_channel = daily_alva_config.slack_channel
bot_emoji = daily_alva_config.bot_emoji
bot_username = daily_alva_config.bot_username

with open('{}/week_names.txt'.format(os.path.dirname(os.path.abspath(__file__)))) as f:
    prev_names = [line.strip() for line in f.readlines()]
    names = [v for v in name_list if v not in prev_names]

name1 = random.choice(names)
names.remove(name1)
name2 = random.choice(names)

p1 = '{} & {} let’s take this relationship to the next level - maybe you can show me something you’re working on?'.format(name1, name2)
p2 = 'Today’s another great day to be working at {} - whatcha doin {} & {}?'.format(company, name1, name2)
p3 = '{} & {}, it’s your time to shine - let us know what you’re working on!'.format(name1, name2)
p4 = '{} & {} hope you are having a great day, wanna share what you are doing today?'.format(name1, name2)
p5 = 'Friday’s are all about me - but let’s make today about you. What’s up {} & {}?'.format(name1, name2)
p6 = 'You’ve been way too quite lately {} & {}, tell us what’s going on today!'.format(name1, name2)

phrases = [p1, p2, p3, p4, p5, p6]

payload = {'text': random.choice(phrases), 'link_names': 1, 'channel': slack_channel, 'icon_emoji': bot_emoji, 'username': bot_username}

response = requests.post(webhook, data=json.dumps(payload))

if response.status_code == 200:
    with open('{}/week_names.txt'.format(os.path.dirname(os.path.abspath(__file__))), 'a') as f:
        f.write(name1 + '\n' + name2 + '\n')
    print(name1, name2)
    y = int(datetime.date.today().strftime('%Y'))
    m = int(datetime.date.today().strftime('%m'))
    d = int(datetime.date.today().strftime('%d'))
    if date(y, m, d).weekday() == 4:
        f = open('{}/week_names.txt'.format(os.path.dirname(os.path.abspath(__file__))), 'w')
        f.truncate()
        f.close()
else:
    print(response.json().get('status'))
