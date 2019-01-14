# post to slack everytime a new excel file with beer releases on systembolaget is avaliable during 2019
# -*- coding: utf-8 -*-
import config
import csv
import json
import logging
import os
import re
import requests
import shutil
logging.basicConfig(filename='systemet.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
systembolaget = 'https://www.systembolaget.se/fakta-och-nyheter/nyheter-i-sortimentet/lanseringar/'
webhook = config.webhook
release_dates = ['18 januari', '1 februari', '15 februari', '8 mars', '22 mars', '5 april', '26 april', '3 maj', '17 maj', '7 juni', '5 juli', '2 augusti', '16 augusti']


systemet_request = requests.get(systembolaget)

result = re.findall('<a href=\"\/imagelibrary\/publishedmedia\/[\w]+\/Sm-_partier_[\w]+(?:[.]xls)?.xlsx\">[\w\s]+<\/a>', systemet_request.text)
for line in result:
    after = line.split('"')[1]
    file_name = after.split('/')[-1]
    csv_file_name = file_name.split('.xlsx')[0]
    url = 'https://systembolaget.se{}'.format(after)
    logging.info(url)
    logging.info(file_name)
    response = requests.get(url, stream=True)
    if os.path.isfile('{}/{}.xlsx'.format(os.path.dirname(os.path.abspath(__file__)), csv_file_name)):
        logging.info("file exists")
    else:
        logging.info('not existing')
        with open('{}/{}.xlsx'.format(os.path.dirname(os.path.abspath(__file__)), csv_file_name), 'wb') as xlsx_file:
            shutil.copyfileobj(response.raw, xlsx_file)

with open('{}/sma_partier.csv'.format(os.path.dirname(os.path.abspath(__file__))), 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    prev_dates = list(reader)

for string in release_dates:
    print('små partier {}'.format(string))
    if 'Små partier {}'.format(string) in systemet_request.text:
        shall_write = False
        if any(string in s for s in prev_dates):
            print('No new releases')
        else:
            shall_write = True
            if shall_write is True:
                with open('{}/sma_partier.csv'.format(os.path.dirname(os.path.abspath(__file__))), 'a', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=';', quotechar='“')
                    csv_writer.writerow([string])
                payload = {'text': 'Nu finns det en ny excel-fil med små partier på Systembolaget den {}! Tryck på länken för att ladda ner filen: {}'.format(string, url)}
                post_slack = requests.post(webhook, data=json.dumps(payload))
                print(post_slack.text)
    else:
        print('No matches')
