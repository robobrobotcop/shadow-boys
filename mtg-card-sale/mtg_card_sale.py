# -*- coding: utf-8 -*-
import json
import requests
from datetime import datetime, timedelta
import mtg_card_sale_config
today = datetime.utcnow()
update = datetime.utcnow() - timedelta(1)

usr = mtg_card_sale_config.usr
pwd = mtg_card_sale_config.pwd
url = mtg_card_sale_config.url
webhook = mtg_card_sale_config.webhook


response = requests.post(url, data="""{
    me {
        name
        inventoryCount
        inventoryValue
        clientFunds
        sold (soldSince: \"$update\") {
            qty
            name
            price
            foil
            lang
        }
        payouts {
            sum
        }
    }
    }""".replace("$update", update.strftime("%Y-%m-%d %H:%M:%S")), auth=(usr, pwd))


cards = ''
for sold_card in response.json()['me']['sold']: 
    card = str(sold_card['qty']) + ' ' + sold_card['name'] + ', ' + str(sold_card['price']) + ' SEK, Language: ' + sold_card['lang'] + ', Foil: ' + str(sold_card['foil']) + '\n'
    cards = ''.join((cards, card))


paid_out = 0
if response.json()['me']['payouts']:
    for payout in response.json()['me']['payouts']:
        paid_out += payout['sum']
else:
    paid_out = 0


payload = {
    'text': '*MTG cards for sale, update {}*'.format(today.strftime("%Y-%m-%d")) + '\n'
    'Cards in inventory: ' + str(response.json()['me']['inventoryCount']) + '\n'
    'Value of inventory: ' + str(response.json()['me']['inventoryValue']) + ' SEK' + '\n'
    'Sum at client funds account (to be paid out): ' + str(response.json()['me']['clientFunds']) + ' SEK' + '\n'
    'Total sum paid out: ' + str(paid_out) + ' SEK' + '\n'
    '*New sold cards:*' + '\n' + str(cards)}

response = requests.post(webhook, data=json.dumps(payload))
