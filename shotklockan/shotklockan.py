# -*- coding: utf-8 -*-
import json
import logging
import random
import requests
logging.basicConfig(filename='systemet.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

url = ''  # input slack webhook
name = ['Hörni allihopa', 'Lauri', 'Emma', 'Carl Oscar', 'Christian', 'Robin', 'Filip', 'Emil', 'Emil', 'Carl Oscar och Emma', 'Lauri och Emil', 'Christian och Filip']
payload = {'text': random.choice(name) + ', det är dags för en shot! :shot: @channel', 'link_names': 1}


response = requests.post(url, data=json.dumps(payload))
logging.info(response.text)
