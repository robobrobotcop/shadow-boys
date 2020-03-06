# -*- coding: utf-8 -*-
import json
import requests
import os
from datetime import datetime, timedelta
from retry import PostFailure, retry
today = datetime.utcnow()
update = datetime.utcnow() - timedelta(1)


@retry(PostFailure)
def get_api_data(user):
    response = requests.post(user['url'], data="""{
        me {
            name
            inventoryCount
            inventoryValue
            clientFunds
            sold (soldSince: \"$update") {
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
        }""".replace("$update", update.strftime("%Y-%m-%d %H:%M:%S")), auth=(user['usr'], user['pwd']))

    if response.status_code not in (200, 403):
        raise PostFailure('error code from api')
    return response


@retry(PostFailure)
def post_to_slack(payload, user):
    response = requests.post(user['webhook'], data=json.dumps(payload))
    if response.status_code != 200:
        raise PostFailure('error code from slack')


with open('{}/mtg_card_sale_config.json'.format(os.path.dirname(os.path.abspath(__file__))), 'r') as fh:
    users = json.load(fh)


for user in users:
    response = get_api_data(user)
    cards = ''
    for sold_card in response.json()['me']['sold']:
        if sold_card['foil']:
            card = str(sold_card['qty']) + ' ' + sold_card['name'] + u', à ' + str(sold_card['price']) + ' SEK, Language: ' + sold_card['lang'] + ', *Foil*' + '\n'
        else:
            card = str(sold_card['qty']) + ' ' + sold_card['name'] + u', à ' + str(sold_card['price']) + ' SEK, Language: ' + sold_card['lang'] + '\n'
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
        '*New sold cards:*' + '\n' + cards,
        'channel': user['channel']}
    if cards != '':
        post_to_slack(payload, user)
